import requests #importerar biblioteket requests
import web #importerar web.py
import ui #importerar ui.py

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" 
artists = web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")["artists"] #artists blir en variabel av svaret man får från apin som skickas till web.py och funktionen get

ui.line()
ui.header("ARTIST DB")
ui.line()
ui.echo("Welcome to a world of")
ui.echo("Music!")
ui.line()
ui.echo(" L | List artists")
ui.echo(" V | View artist profile")
ui.echo(" E | Exit application")
ui.line()
selection = ui.prompt("Selection >") #en input av användaret som bestämmer vad man vill göra

while True:
    if selection.lower() == "l": #om inputen är l
        ui.line()
        ui.header("ARTIST DB")
        ui.line()
        for i in artists: #för varje plats i listan artists
            ui.echo(i["name"])
        ui.line(True)
        ui.echo(" L | List artists")
        ui.echo(" V | View artist profile")
        ui.echo(" E | Exit application")
        ui.line()
        selection = ui.prompt("Selection >") #tar in en ny input så att programmet kan fortsätta

    if selection.lower() == "v": #om inputen är v
        ui.line()
        ui.header("ARTIST DB")
        ui.line()
        name = ui.prompt("Artist name >") #tar in en input på vilken artist man vill veta mer om
        for i in artists: #för varje plats i listan artists
            if name.lower() == i["name"].lower(): #om namnet i inputen matchar namnet i listan
                url2 = url + str(i["id"]) #görs en ny url
                APIresponse = web.get(url2) #sätter variabeln APIresponse lika med svaret man får från apin som går genom web.py i funktionen get
                genres = APIresponse["artist"]["genres"]
                members = APIresponse["artist"]["members"]
                ui.line(True)
                ui.header(i["name"]) #skriver ut artistens namn
                ui.header("Members:")
                for i in members: #för varje plats i listan members
                    ui.echo(i) #skrivs varje plats (varje medlem) ut
                ui.header("Genres:")
                for i in genres: #för varje plats i listan genres
                    ui.echo(i) #skrivs varje plats (varje genre) ut
                ui.echo("Years active: " + APIresponse["artist"]["years_active"][0])
                ui.line(True)
                ui.echo(" L | List artists")
                ui.echo(" V | View artist profile")
                ui.echo(" E | Exit application")
                ui.line()
                selection = ui.prompt("Selection >") #tar in en ny input så att programmet kan fortsätta

    if selection.lower() == "e": #om inputen är e
        ui.echo("Exiting the application")
        break #stängs programmet av