##pip install pyTelegramBotAPI
##telegram - BotFather - token

#import telebot

#bot = telebot.TeleBot("xxx",)

#@bot.message_handler(content_types=['text'])
## функция def send_echo будет вызываться всегда, когда в телеге будет набран
## тип данных (контента) - текст (не картинка и др)

#def send_echo(message):
        ##эта функция принимает один параметр - message
	##bot.reply_to(message, message.text) #так бот отвечает с цитатой
        #bot.send_message(message.chat.id,message.text)#так просто эхо

##запускаем бота с аргументом (none_stop = True)
#bot.polling(none_stop = True)

###############################
from pyowm import OWM
import telebot

owm = OWM('6c5f43af9fa85cb25be96649e9249bed')
mgr = owm.weather_manager()
bot = telebot.TeleBot("xxx",)



@bot.message_handler(content_types=['text'])
def send_echo(message):
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temp = w.temperature('celsius')['temp']

        answer = "In " + message.text + " now there are " + w.detailed_status+'.'+ "\n"
        # += быстрая конкатенация
        answer += "And the temperature outside is about " + str (temp) + " degrees." + "\n\n"
        if temp <=10:
                answer += ("Its too cold to go withought a hat weared on!")
        elif temp >10 and temp < 25:
                answer += ('You could go outside withought a hat.')
        else:
                answer += ("You can weare shorts or nothing!")
        
        bot.send_message(message.chat.id, answer)

#запускаем бота с аргументом (none_stop = True)
bot.polling(none_stop = True)
print("Hello, World!")

