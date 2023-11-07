from flask import Flask
from flask import render_template
from flask import url_for
from datetime import datetime
import random

app = Flask(__name__)

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


@app.route('/order')
def make_order():
    return render_template('order.html')

if __name__ == '__main__':
    app.run(port=8086, debug=True)