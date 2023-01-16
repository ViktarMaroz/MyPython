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

