print("Hur gammal är du?")
ålder = int(input()) #får in en input av din ålder
årtillmyndig = 18 - ålder
årfrånmyndig = ålder - 18
if ålder < 18 : #om du är under 18 så skrivs det ut hur många år det är tills du är myndig
    print("Du är myndig inom " + str(årtillmyndig) + " år!")
elif ålder > 18 :#om du är myndig skrivs det ut hur länge du har varigt myndig
    print("Du har varit myndig i " + str(årfrånmyndig) + " år!")
elif ålder == 18 : #om du är 18 skrivs det ut att du nyligen blivit myndig
    print("Du blev myndig nyligen")