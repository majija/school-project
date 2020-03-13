import telebot
import sqlite3, pandas as pd, numpy as np
bot = telebot.TeleBot('1126985690:AAHWxfz1vj20NO2eoLN-093L0Pd7bc8xEu0')  # Сюда нужно вставлять токен каждый раз
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
database = pd.read_sql("""SELECT * FROM users""", conn)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, познакомимся?')


@bot.message_handler(commands=['create_profile'])
def create_user(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    username = message.from_user.username
    rating = 5.0
    id = 1
    string_to_add = (str(id) + ', ' + str(username) + " , '" + str(rating) + "'")
    print(string_to_add)
    if len(database.nickname.loc[database.nickname == username]) == 0:
        cursor.execute("""INSERT INTO users
                      VALUES ('{}', '{}', {})""".format(id, username, rating)
                       )
        conn.commit()
        bot.send_message(message.chat.id, 'Я вас зарегистрировал!')
    else:
        bot.send_message(message.chat.id, 'Вы уже зарегестрированы!')

bot.polling()