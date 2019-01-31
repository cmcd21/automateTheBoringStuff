#! python3
#quickWeather.py - Prints the weather for a location from the command line

import json, requests, sys

'''
#compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
'''

location = 'Belfast'

#download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=e070fd6ac25eede9181a041c78c57b35' % (location)
response = requests.get(url)
response.raise_for_status()

#load JSON data into a Python variable
weatherData = json.loads(response.text)

#print weather descriptions
w = weatherData['weather']
print('Current weather in %s: ' % (location))
print(w[0]['main'], '-', w[0]['description'])
