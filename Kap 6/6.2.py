import requests #importerar biblioteket requests

print("Enter the cities name")
city = str(input()) #tar in en input på en stad

try: #försöker köra koden nedan annars om programmet kraschar går den till except (ifall att staden inte finns)
    url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + city.lower() #lägger till staden i små bokstäver
    r = requests.get(url)
    APIresponse = r.json() #APIresponse blir variabeln för vad man får ut från apiet
    forecasts = APIresponse["forecasts"] #går in i nyckelordet forecasts
    print("Forecasts: ")
    for i in forecasts: #för varje plats i listan forecast
        print(i["date"] + " is prognosed to be " + i["forecast"]) #skrivs varje datum och och respektive prognos ut
except: #om programmet krashar så körs koden nedan
    print("Invalid city")