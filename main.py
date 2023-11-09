from flask import Flask
from flask import render_template, request
from flask import url_for
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

@app.route('/menu/')
def show_menu():
    context = {
        'pizzas': menu_pizza
    }
    return render_template('menu.html', **context)


@app.route("/order", methods=["GET", "POST"])
def make_order():
    if request.method == 'POST':
        pizza_name = request.form['pizza_name']
        pizza_count = request.form['pizza_count']
        delivery_adress = request.form['delivery_adress']
        phone_number = request.form['phone_number']
        with sqlite3.connect("sqlite_python_oderman2.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO order_db (pizza_name,pizza_count,delivery_adress,phone_number) VALUES (?,?,?,?)", (pizza_name, pizza_count, delivery_adress, phone_number))
        users.commit()
        return render_template("index.html")
    else:
        return render_template('order.html')

    # @app.route('/participants')
    # def participants():
    #     connect = sqlite3.connect('database.db')
    #
    # cursor = connect.cursor()
    # cursor.execute('SELECT * FROM PARTICIPANTS')
    #
    # data = cursor.fetchall()
    # return render_template("order.html", data=data)




if __name__ == '__main__':
    app.run(port=8086, debug=True)