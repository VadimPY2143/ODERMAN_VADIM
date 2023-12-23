from flask import Flask
from flask import render_template, request
from flask import url_for, redirect, flash, abort
from datetime import datetime
import sqlite3
import requests
from requests import get
import random

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect(database='sqlite_python_oderman.db')
    connection.row_factory = sqlite3.Row
    return connection


@app.route('/')
def horoskope():
    return render_template('index.html')


pizza_list = []
connection = get_db_connection()
pizzas = connection.execute('SELECT * FROM pizza_menu').fetchall()
for p in pizzas:
    pizza_list.append(p['name'])


@app.route('/menu/')
def show_menu():
    connection = get_db_connection()
    pizzas = connection.execute('SELECT * FROM pizza_menu').fetchall()
    return render_template('menu.html', pizzas = pizzas)


@app.route("/order", methods=["GET", "POST"])
def make_order():
    if request.method == 'POST':
        pizza_name = request.form['pizza_name']
        pizza_count = request.form['pizza_count']
        delivery_adress = request.form['delivery_adress']
        phone_number = request.form['phone_number']
        with sqlite3.connect("sqlite_python_oderman.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO order_db (pizza_name,pizza_count,delivery_adress,phone_number) VALUES (?,?,?,?)", (pizza_name, pizza_count, delivery_adress, phone_number))
        users.commit()
        return render_template("index.html")
    else:
        return render_template('order.html')

@app.route('/create', methods = ['GET', 'POST'])
def create_pizza():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']

        if not name:
            flash('Pizza name is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO pizza_menu (name, price) VALUES (?,?)', (name,price))
            connection.commit()
            connection.close()
            return render_template('index.html')

    return render_template('create.html')


def get_current_weather(city):
    API_KEY = 'bddebc304257efa7289dcdb93bebeee5'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data

    else:
        return None



@app.route('/weather')
def weather():
    return render_template('weather_form.html')


@app.route('/weather_result',  methods = ['GET', 'POST'])
def weather_result_show():
    if request.method == 'POST':
        city = request.form['city']
        answer = get_current_weather(city)
        pizza_recommendation = random.choice(pizza_list)
        return render_template('weather_show.html', data = answer, pizza_r = pizza_recommendation)
    


poll_data = {
    'question': 'Чи подобається вам наша піца?',
    'choice': ['Так','Ні']
}

@app.route('/poll1')
def start_poll():
    return render_template('poll.html', data = poll_data)

@app.route('/poll')
def poll():
    return render_template('thankyou.html', data = poll_data)



if __name__ == '__main__':
    app.run(port=8086, host="0.0.0.0", debug=True)