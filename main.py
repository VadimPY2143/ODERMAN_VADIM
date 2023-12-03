from flask import Flask
from flask import render_template, request
from flask import url_for, redirect, flash, abort
from datetime import datetime
import sqlite3


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

def get_db_connection():
    connection = sqlite3.connect(database='sqlite_python_oderman.db')
    connection.row_factory = sqlite3.Row
    return connection


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


if __name__ == '__main__':
    app.run(port=8086, debug=True)