# PROJECT 02: WEATHER APP

# Modules to be installed:
# 1. pip install requests
# 2. pip install pywin32 (installing name) and import as "win32com.client"

import requests
# by importing this module we can use/import anything via network/internet

import json
# this is a built-in module, using this module to use 'json.loads()' function so that with his help I can parse a dictionary

import win32com.client as wincom
#importing this windwos module in python for speaking

# now go to 'https://www.weatherapi.com/my/' copy the API (Application Programming Interfaces) key and paste it on 'http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=delhi' ;now all the weather details will be shown to you.
# now let's read all the kolkata weather details here details here
#we can choose any city

city=input("Enter the name of the city:")
url=f"https://api.weatherapi.com/v1/current.json?key=0e21a9b3c1694de6836131753231104&q={city}"
r= requests.get(url)
print(r.text)
print(type(r.text))    #it is a string

wdict= json.loads(r.text)
#json.loads func loads a string; pronounsed as j son dot load s / loads; wdict is short name for weather dictionary
w=wdict["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(f"'The current weather in {city} is {w} degrees'")
print(wdict["current"]["temp_c"])