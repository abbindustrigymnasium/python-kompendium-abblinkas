male = [
"Erik", 
"Lars", 
"Karl",
"Anders",
"Johan"
]
female = [
"Maria",
"Anna",
"Margareta", 
"Elisabeth",
"Eva" 
]
print("Vilket namn ska plockas bort från listorna")
namn = str(input())
if namn in male:
    male.remove(namn)
    print ("Män:", male)
    print ("Kvinnor:", female)
elif namn in female:
    female.remove(namn)
    print ("Män:", male )
    print ("Kvinnor:", female) 
else:
    print("Namnet finns inte med i någon av listorna")


