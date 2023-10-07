from flask import Flask
from flask import render_template
from flask import url_for
from datetime import datetime
import random

app = Flask(__name__)


mas = ['Сьогодні вас чекає гарний день', 'Завтра вас чекає поганий день', 'Вам підвищать зарплату', 'Вас чекають маленькі неприємності']


@app.route('/')
def horoskope():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8086, debug=True)