from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# из библиотеки flask_sqlalchemy импортирует класс SQLAlchemy
# render_template функция для работы с HTML
# url_for фкнкция шаблонизатора
app = Flask(__name__)  # передаем конструктором обекта класса __name__ имя этого файла
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# обращаемся к словорю config по клучу 'SQL..' и указыкаем бд с которой будем работать (у нас sqlite)
# создаем бд с названием blog.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Отключаем SQLALCHEMY_TRACK_MODIFICATIONS что бы не всплывала ошибка о том что это скоро перестанут поддерживать
db = SQLAlchemy(app)
# создаем объект на основе класса SQLAlchemy передаем в него обэект класса flask - app
# в котором настроено подключение к бд

# создаем класс Article наследуемый от объекта db
# с помощью Article будем создавать таблицу и управлять ей для нашей дб
# создаем колонки в таблице


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id
    # с помощью магического метода repr указываем что когда мы выбираем обьект основе этого класса
    # нам будет выдаваться сам объект и его id


"""для установки бд в терминале откываем python
from app import db
db.create_all()"""


@app.route('/')  # с помощью декоратора и функции (route) указываем путь который хотим отслеживать
# ('/' - главная страница)
@app.route('/home')
def index():  # создаем свою функцию для отслеживания страницы
    return render_template('index.html')  # выводим файл с html шаблоном, по умолчанию в папке teamplates


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create-article', methods=['POST', 'GET'])
# указываем методы которые обрабатывает функция
# GET переход на страницу
# POST отправление статей
def create_article():
    if request.method == 'POST':
        # получаем данные
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        # передаем данные в новый обьект на основе класса Article

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article) #  добавляем объект article в бд
            db.session.commit() #  сохраняем объект
            return redirect('/') #  с помощью функции redirect после добавления статьи перенаправляемся на главную страницу
        except:
            return "При добавлении статьи произошла ошибка"
    else:
        return render_template('create-article.html')


if __name__ == '__main__':  # если запускаем через этот файл(app.py) = то запускаем проект как flask приложение
    app.run(debug=True)  # run() запускает сервер * debug=True - выведет ошипки при запуске на страничке
    # в прод. уст. False !!
