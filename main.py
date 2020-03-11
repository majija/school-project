import telebot
import sqlite3
bot = telebot.TeleBot()  # Сюда нужно вставлять токен каждый раз
conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, познакомимся?')


@bot.message_handler(commands=['create_profile'])
def create_user(message):
    bot.send_message(message.chat.id, 'Привет, познакомимся?')
    username = message.from_user.username
    rating = 5.0
    string_to_add = ('10, ' + str(rating) + ", '" + str(username) + "'")
    cursor.execute("""INSERT INTO table1  (a, b, c)
                   VALUES
                   """)



bot.polling()