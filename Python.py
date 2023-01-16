#скачать с сайта https://www.python.org и установить
#cmd - python -v запуск IDLE
#запуск пайтон файла с cmd - преходим в нужную дир. (просмотр сод каталогоа - dir)
#апускаем python file.py
#float
fnumber =5.2
#str
name = "Viktar"
#bool (с большой буквы)
status = True
#####################################
#функция print аргумент ()
print("bad guy")
#выполнить - F5
print (fnumber)
#Экранирование функиции print - \
print ("Он \"плохой\" человек!")
#можно и в разные кавычки без экранирования
print ('Он "плохой" человек!')
#перевод строки спец символ \n
print ('Hello \nWorld!')
#а можно и так
print ('Hello')
print ('World!')
##################################
#Конкатенация +
print ('Hello, my name is ' + name+'!')
#Type casting - перевод переменной из 1 вида в другой напримар фнкции:
# в стрингу str /в вещ float /целочисл int/булево bool 
age = 38
print (" I am "+str(age) + ' years old')
###################################
#функция input - возвращает все стрингом str!!!
#name = input('Hello! Enter your name please:')
#age = input('Now, please, enter you age:')

#print ('Hello' + name+'!')
#print ('You\'re ' +age+ ' years, that\'s cool!')
##################################
#+,-,*,/,**(степень),%(деление по модулю), унарный минус, округление, Пи
a=5
b=10
c=a+b
print (c)
c=a-b
print (c)
c=b/a
print (c)
c=a%b
print (c)
c=a**2
print (c)
c=-c
print (c)
#в пингпонге что бы отбивалось от стенок
z=2.225
print(z)
print (round(z))
#округление в меньшую math.floor()/большую math.ceil() сторону.
#Используем фуркцию (модуль) math.Для этого его нужно импортировать - import math
import math
z=2.2665
print (math.floor(z))
print (math.ceil(z))
#пи - math.pi
import math

print (math.pi)

#Дебильный калькулятор v1.0
what = input('Что делаем? (+,-): ')
a= float(input('Введите первое число: '))
b= float(input('Введите второе число: '))
if what=='+':
     c=a+b
     print("Результат: " + str(c))
elif what=='-':
     c=a-b
     print("Результат: " + str(c))
#elif what=="-": - тогда если выполниться один из вышестоящих блоков
#нижеследующие не прогоняются
else:
    print ("Выбрана неверная операция!")
#========================================================
    #Дебильный калькулятор v2.0
#РАбота с модулями (pip менеджер модулей для пайтона)
#https://pypi.org/project/colorama/ - pip install colorama - В cmd  устанавливаем
#init - запуск демона/службы/сервиса - импортируем инит из колорамы
from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.RED)
print (Back.GREEN)
#print(Style.DIM + 'and in dim text')
print(Style.BRIGHT)

what = input('Что делаем? (нажмите + или - или / или *): ')
print (Back.YELLOW)
a= float(input('Введите первое число: '))
b= float(input('Введите второе число: '))

if b==0:
    print(Fore.WHITE)
    print (Back.RED)
    print ("На НОЛЬ делить нельзя!")
else:
     if what=='+':
         c=a+b
         print (Back.WHITE)
         print("Результат: " + str(c))
     elif what=='-':
          c=a-b
          print("Результат: " + str(c))
     elif what=='/': 
          c=a/b
          print("Результат: " + str(c))
     elif what=='*': 
          c=a*b
          print("Результат: " + str(c))
     else:
          print(Fore.WHITE)
          print (Back.RED)
          print ("Выбрана неверная операция!")
input ()
#===============
# установим компилятор
#pip install pyinstaller    в cmd
# cобираем - pyinstaller -F crazy_calculator.py
=====================================

#https://openweathermap.org/  - API можно использовать
#можно использовать pip pyown - pip install pyowm в cmd
from colorama import init
from colorama import Fore, Back, Style
init()
print (Back.GREEN)
print(Fore.BLACK)

place = input("Wich City/Country are you interested?: ")
              
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('6c5f43af9fa85cb25be96649e9249bed')
mgr = owm.weather_manager()

#reg = owm.city_id_registry()
#list_of_locations = reg.locations_for('moscow', country='RU')
#moscow = list_of_locations[0]
#lat = moscow.lat   # 55.75222
#lon = moscow.lon   # 37.615555

observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')['temp']

print (Back.YELLOW)
print(Fore.BLACK)
print ("In " + place + " now there are " + w.detailed_status+'.')
print ("And the temperature outside is about " + str (temp) + " degrees.")
print (Back.WHITE)
if temp <=10: print ("Its too cold to go withought a hat weared on!")
elif temp >10 and temp < 25: print ('You could go outside withought a hat.')
else: print ("You can weare shorts or nothing!")
input ()
==========================





