import requests
import web
import ui

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
artists = web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")["artists"]

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
selection = ui.prompt("Selection >")

while True:
    if selection.lower() == "l":
        ui.line()
        ui.header("ARTIST DB")
        ui.line()
        for i in artists:
            ui.echo(i["name"])
        ui.line(True)
        ui.echo(" L | List artists")
        ui.echo(" V | View artist profile")
        ui.echo(" E | Exit application")
        ui.line()
        selection = ui.prompt("Selection >")

    if selection.lower() == "v":
        ui.line()
        ui.header("ARTIST DB")
        ui.line()
        name = ui.prompt("Artist name >")
        for i in artists:
            if name.lower() == i["name"].lower(): 
                artistid = i["id"]
                url2 = url + str(artistid)
                APIresponse = web.get(url2)
                genres = APIresponse["artist"]["genres"]
                members = APIresponse["artist"]["members"]
                ui.line(True)
                ui.header(i["name"])
                ui.header("Members:")
                for i in members:
                    ui.echo(i)
                ui.header("Genres:")
                for i in genres:
                    ui.echo(i)
                ui.echo("Years active: " + APIresponse["artist"]["years_active"][0])
                ui.line(True)
                ui.echo(" L | List artists")
                ui.echo(" V | View artist profile")
                ui.echo(" E | Exit application")
                ui.line()
                selection = ui.prompt("Selection >")

    if selection.lower() == "E":
        ui.header("Exiting the application")
        break