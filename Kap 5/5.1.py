Daniel_Radcliffe = ["man", "brun", "brun", "Daniel Radcliffe"]
Rupert_Grint = ["man", "röd", "blå", "Rupert Grint"]
Emma_Watson = ["kvinna", "brun", "brun", "Emma Watson"]
Selena_Gomez = ["kvinna", "brun", "brun", "Selena Gomez"]
Linus_Kasper = ["man", "blond", "brun", "Linus Kasper"]
Lindrit_Koxha = ["man", "brun", "brun", "Lindrit Koxha"]
#listor av "kändisar" med dera utseenden

kändisar = [Daniel_Radcliffe, Rupert_Grint, Emma_Watson, Selena_Gomez, Linus_Kasper, Lindrit_Koxha]
lookalikes = ""
#lista med alla "kändisars" egna listor samt en tom string

print("Ange kön:")
kön = str(input())
print("Ange hårfärg:")
hårfärg = str(input())
print("Ange ögonfärg:")
ögonfärg = str(input())
#inputs för information om användaren

for personer in kändisar: #för varje plats i listan kändisar som är en kändis egen lista
    if personer[0] == kön: #om användarens inmatning matchar med kändisens utseende
        if personer[1] == hårfärg: #om användarens inmatning matchar med kändisens utseende
            if personer[2] == ögonfärg: #om användarens inmatning matchar med kändisens utseende
                lookalikes += personer[3] + ", " #om det gör det så lägger den till kändisens namn i den tomma stringen

if lookalikes == "": #om den tomma strängen fortfarande är tom skrivs det ut att användaren inte matchar med någon kändis
    print("Du liknar dessvärre ingen kändis...")
else:
    print("Du liknar " + lookalikes + "!") #om den tomma strängen nu har blivit fylld med matchande kändisar skrivs det ut vilka kändisar som du matchar med