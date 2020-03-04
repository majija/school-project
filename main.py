import telebot
bot = telebot.TeleBot('1126985690:AAHWxfz1vj20NO2eoLN-093L0Pd7bc8xEu0')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, познакомимся?')


bot.polling()