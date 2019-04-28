multitab = int(input("Ange en multiplikationstabell")) #tar in en input på vilken multiplikationstabell programmet ska använda
number = 0 #variabel som håller koll på antal gånger programmet skriver ut talen
numberoftimes = 3 #antal gånger talen i multiplikationstabellen skrivs ut
tot = multitab #en variabel som kommer vara det tal som skrivs ut, det börjar vara lika med multitab eftersom det är det första talet

while True: #körs till programmet breakas
    print(tot) #printar första talet i multiplikationtabellen
    tot += multitab #tot lägger på multitab som blir nästa tal i tabellen
    number += 1 #lägger på 1 i minnet
    if number == numberoftimes: #om minnet är lika med numberoftimes
        answer = str(input("Fortsätt? ")) #tar in en input och frågar om användaren vill forsätta
        if answer.lower() == "ja": #om svaret är ja
            numberoftimes += 3 #lägger till 3 på number of times variabel som gör att programmet kommer skriva ut 3 igen
            continue #forsätter while loopen
        else: #annars
            break #stänger av while loopen