import telebot
bot = telebot.TeleBot()  # Сюда нужно вставлять токен каждый раз


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, познакомимся?')


bot.polling()