#pip install pyTelegramBotAPI
#telegram - BotFather - token

import telebot

bot = telebot.TeleBot("1721318464:AAHEZkKBYr_rCbimh2m12Fucb2LgXQsacp0",)

@bot.message_handler(content_types=['text'])
# функция def send_echo будет вызываться всегда, когда в телеге будет набран
# тип данных (контента) - текст (не картинка и др)

def send_echo(message):
        #эта функция принимает один параметр - message
	bot.reply_to(message, message.text)

#запускаем бота с аргументом (none_stop = True)
bot.polling(none_stop = True)
