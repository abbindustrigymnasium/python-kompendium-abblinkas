#Använder en gammal uppgift fast importerar en modul från web.py
import web
import requests

print("Enter the cities name")
city = str(input())

cities = [
    "stockholm", 
    "uppsala",
]

if city.lower() in cities:
    APIresponse = web.get('https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + city.lower())
    forecasts = APIresponse["forecasts"]
    print("Forecasts: ")
    print(forecasts[0]["date"] + " is prognosed to be " + forecasts[0]["forecast"] )
    for i in forecasts:
        print(i["date"] + " is prognosed to be " + i["forecast"])
else:
    print("Invalid city")