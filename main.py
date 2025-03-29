import win32com.client as wincom
import requests
import json

speak = wincom.Dispatch("SAPI.SpVoice")



city = input("Enter the name of the city")

url = f"http://api.weatherapi.com/v1/current.json?key=16bda1d13971474cb7c94933252903&q={city}"


r = requests.get(url)





wdic = json.loads(r.text)


w = wdic["current"]["temp_c"]

win = wdic["current"]["wind_mph"]


text = f"The current weather in {city} is {w} degrees"
wind_text = f"The Wind Speed in Miles Per Hour (mph) in {city} is {win}"
speak.Speak(text)
speak.Speak(wind_text)

















