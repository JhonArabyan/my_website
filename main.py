from flask import Flask
import random
app = Flask(__name__)
facts = ['Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.', 'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.', 'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.']
@app.route("/")
def hello_world():
    return '<p>Здесь факты</p> <a href="/facts">Посмотреть случайный факт!</a> <a href="/secret_page">Сгенерировать пароль!</a>'
@app.route('/facts')
def my_facts():
    return f'<h1>{random.choice(facts)}</h1>'
@app.route('/secret_page')
def secret():
    symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    len2 = 5
    password = ''
    for i in range(len2):
        password += random.choice(symbols)
    return '<img src = "https://avatars.mds.yandex.net/i?id=c1730bc14242684635498f9a76d93fdd_l-9106782-images-thumbs&n=13"' \
    ' alt="Image"' \
    'width=10%>' f'<p>{password}</p>'
app.run(debug=True)
