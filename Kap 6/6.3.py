import requests #importerar biblioteket requests
print("---ARTIST DB---")

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

r = requests.get(url)
APIresponse = r.json()
artists = APIresponse["artists"] #sätter variabeln artists till listan artist i apin

for i in artists: #för varje plats i listan artists
    print(i["name"]) #skrivs namnen ut

print("-------------")
print("Select artist:")
name = str(input()) #tar in en input på en vald artists
print("-------------")

for i in artists: #för varje plats i listan artists
    if i["name"] == name.title(): #om inputen matchar en av artisterna i listan
        artistid = i["id"] #hämtar id
        url2 = url + str(artistid) #gör en ny url
        r = requests.get(url2)
        APIresponse = r.json() #APIresponse blir listan som man får från apit
        genres = APIresponse["artist"]["genres"]
        members = APIresponse["artist"]["members"]
        name = APIresponse["artist"]["name"]
        print(name)
        print("*************")
        print("Genres: ")
        for i in genres: #för varje plats i listan för genrer
            print(i) #skrivs varje genre ut
        print("Years active: " + APIresponse["artist"]["years_active"][0])
        print("Members: ")
        for i in members: #för varje plats i listan för members
            print(i) #skrivs varje member ut
        print("-------------")