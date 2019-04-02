norden = ["Danmark", "Finland", "Island", "Norge", "Sverige"]
storbritannien = ["England", "Nordirland", "Skottland", "Wales"]
print("Ange ett land: ")
land = str(input())
if land.title() in norden :
    print(land.title() + " ligger i Norden.")
elif land.title() in storbritannien :
    print(land.title() + " ligger i Storbritannien.")
else:
    print(land.title() + " ligger varken i Norden eller Storbritannien")