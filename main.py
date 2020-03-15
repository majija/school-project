import numpy as np
import pandas as pd
import sqlite3
import settings

import telebot

bot = telebot.TeleBot(settings.token)  # Сюда нужно вставлять токен каждый раз
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
    if len(database.nickname.loc[database.nickname == username]) != 0:
        bot.send_message(message.chat.id, 'Вы уже зарегестрированы!')
    else:
        id = len(database) + 1
        string_to_add = (str(id) + ', ' + str(username) + " , '" + str(rating) + "'")
        print(string_to_add)
        cursor.execute("""INSERT INTO users
                             VALUES ('{}', '{}', {})""".format(id, username, rating)
                       )
        conn.commit()
        data_size = len(database)
        database.loc[data_size] = [id, username, rating]
        bot.send_message(message.chat.id, 'Я вас зарегистрировал!')


bot.polling()