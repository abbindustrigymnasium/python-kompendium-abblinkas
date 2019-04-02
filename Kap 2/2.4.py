# Övningsuppgift 2.4

print("Hur gammal är du?")
ålder = int(input())
årtillmyndig = 18 - ålder
årfrånmyndig = ålder - 18
if ålder < 18 :
    print("Du är myndig inom " + str(årtillmyndig) + " år!")
elif ålder > 18 :
    print("Du har varit myndig i " + str(årfrånmyndig) + " år!")
elif ålder == 18 :
    print("Du blev myndig nyligen")