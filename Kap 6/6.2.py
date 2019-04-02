import requests

print("Enter the cities name")
city = str(input())

cities = [
    "stockholm", 
    "uppsala",
]

if city.lower() in cities:
    url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + city.lower()
    r = requests.get(url)
    APIresponse = r.json()
    forecasts = APIresponse["forecasts"]
    print("Forecasts: ")
    print(forecasts[0]["date"] + " is prognosed to be " + forecasts[0]["forecast"] )
    for i in forecasts:
        print(i["date"] + " is prognosed to be " + i["forecast"])
else:
    print("Invalid city")