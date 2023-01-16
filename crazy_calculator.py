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
input()

          
