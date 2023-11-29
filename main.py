import telebot

bot = telebot.TeleBot('6586553259:AAHler9d6E6FQJx2he8hC0I8EYbTAKZWDKw')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет фанатам Масюни')


@bot.message_handler(commands=['xD'])
def main(message):
    bot.send_message(message.chat.id, 'Любишь Масюню?')


bot.infinity_polling()





