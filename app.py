from flask import Flask, render_template, url_for
# render_template функция для работы с HTML
# url_for фкнкция шаблонизатора
app = Flask(__name__)  # передаем конструктором обекта класса __name__ имя этого файла


@app.route('/')  # с помощью декоратора и функции (route) указываем путь который хотим отслеживать
# ('/' - главная страница)
@app.route('/home')
def index():  # создаем свою функцию для отслеживания страницы
    return render_template('index.html')  # выводим файл с html шаблоном, по умолчанию в папке teamplates


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')  # получаем данные их адреса
def user(name, id):
    return 'User page: ' + name + ' - ' + str(id)


if __name__ == '__main__':  # если запускаем через этот файл(app.py) = то запускаем проект как flask приложение
    app.run(debug=True)  # run() запускает сервер * debug=True - выведет ошипки при запуске на страничке
    # в прод. уст. False !!
