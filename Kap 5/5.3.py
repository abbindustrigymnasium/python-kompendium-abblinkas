norden = ["Danmark", "Finland", "Island", "Norge", "Sverige"] #listor med länderna i storbritannien
storbritannien = ["England", "Nordirland", "Skottland", "Wales"] #listor med länderna i norden


print("Ange ett land: ")
land = str(input()) #input på ett land

if land.title() in norden : #om landet ligger i norden(om landet finns med i listan för norden) skrivs det ut
    print(land.title() + " ligger i Norden.")
elif land.title() in storbritannien : #om landet ligger i storbritannien(om landet finns med i listan för storbritannien) skrivs det ut
    print(land.title() + " ligger i Storbritannien.")
else: #annars om landet inte ligger i norden eller storbritannien så skrivs det ut
    print(land.title() + " ligger varken i Norden eller Storbritannien")