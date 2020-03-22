import numpy as np
import pandas as pd
import sqlite3
import settings

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
    number_of_ratings = 1
    if len(database.nickname.loc[database.nickname == username]) != 0:
        bot.send_message(message.chat.id, 'Вы уже зарегестрированы!')
    else:
        id = len(database) + 1
        string_to_add = (str(id) + ', ' + str(username) + " , '" + str(rating) + "'")
        print(string_to_add)
        cursor.execute("""INSERT INTO users
                             VALUES ('{}', '{}', {}, {})""".format(id, username, rating, number_of_ratings)
                       )
        conn.commit()
        data_size = len(database)
        database.loc[data_size] = [id, username, rating]
        bot.send_message(message.chat.id, 'Я вас зарегистрировал!')


@bot.message_handler(commands=['rate'])
def rate_user(message):
    bot.send_message(message.chat.id, 'Кому и какую оценку вы хотите поставить?')

    @bot.message_handler(content_types=['text'])
    def person(message):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        new_user_rate, user_id = (message.text).split()
        cursor.execute("""SELECT rating FROM users WHERE id = {}""".format(int(user_id)))
        user_rating = cursor.fetchall()
        cursor.execute("""SELECT number_of_ratings FROM users WHERE id = {}""".format(int(user_id)))
        rating_numbers = cursor.fetchall()
        cursor.execute(""" UPDATE users SET rating = {} WHERE id = {} """.format(
            (float(new_user_rate) + (user_rating[0][0])) / (rating_numbers[0][0] + 1), user_id))
        cursor.execute(
            """ UPDATE users SET number_of_ratings = {} WHERE id = {} """.format((rating_numbers[0][0] + 1), user_id))
        conn.commit()


bot.polling()
