import telebot
import sqlite3
bot = telebot.TeleBot('')  # Сюда нужно вставлять токен каждый раз
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, познакомимся?')


@bot.message_handler(commands=['create_profile'])
def create_user(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    bot.send_message(message.chat.id, 'Привет, познакомимся?')
    username = message.from_user.username
    rating = 5.0
    id = 1
    string_to_add = (str(id) + ', ' + str(username) + " , '" + str(rating) + "'")
    print(string_to_add)
    cursor.execute("""INSERT INTO users
                      VALUES (1, '{}', {})""".format(username, rating)
                   )
    conn.commit()



bot.polling()