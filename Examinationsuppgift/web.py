import requests #importerar bibliteket requests

def get(url): #en funktion som ska ge ut svaret i apiet för respektive url man har som argument
    APIresponse = requests.get(url).json()
    return APIresponse #returnerar svaret, detta görs för att man kan sätta en variabel som är lika med funktionen