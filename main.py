from flask import Flask
from flask import render_template
from flask import url_for
from datetime import datetime
import random

app = Flask(__name__)


mas = ['Сьогодні вас чекає гарний день', 'Завтра вас чекає поганий день', 'Вам підвищать зарплату', 'Вас чекають маленькі неприємності']

menu_pizza=[
    {'pizza': 'Карбонара', 'price': 300},
    {'pizza': 'Пеппероні', 'price': 250},
    {'pizza': 'Салямі', 'price': 249},
    {'pizza': 'Гавайська', 'price': 200}
]


@app.route('/')
def horoskope():
    return render_template('index.html')

@app.route('/menu/')
def show_menu():
    context = {
        'pizzas': menu_pizza
    }
    return render_template('menu.html', **context)


if __name__ == '__main__':
    app.run(port=8086, debug=True)