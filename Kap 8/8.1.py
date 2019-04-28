def km_to_miles(dist): #funktion för omvandling från km till miles som behöver ha in en distance som argument
    return str(dist*0.6213712) + " miles"  #omvandlar längden och lägger till miles och returnerar en färdig string med den nya längden

def miles_to_km(dist): #funktion för omvandling från miles till km som behöver ha in en distance som argument
    return str(dist*1.609344) + " km" #omvandlar längden och lägger till km och returnerar en färdig string med den nya längden

distance = input("Ange distans") #tar in en input på en distans

if "km" in distance.lower(): #om km finns med i inputen
    length = km_to_miles(float(distance.strip("km"))) #så stripas strängen km bort("km" tas bort från strängen) och skickas sedan till funktionen

elif "miles" in distance.lower(): #om miles finns med i inputen
    length = miles_to_km(float(distance.strip("miles"))) #så stripas strängen miles bort("miles" tas bort från strängen) och skickas sedan till funktionen

print(distance + " motsvarar " + length) #skriver ut vad den origanala längden motsvarar i den andra enheten