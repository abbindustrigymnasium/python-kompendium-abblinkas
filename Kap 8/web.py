import requests

def get(url):
    r = requests.get(url)
    APIresponse = r.json()
    return APIresponse