male = [ #en lista med mansnamn
"Erik", 
"Lars", 
"Karl",
"Anders",
"Johan"
]

female = [ #en lista med flicknamn
"Maria",
"Anna",
"Margareta", 
"Elisabeth",
"Eva" 
]

print("Vilket namn ska plockas bort från listorna")
namn = str(input()) #tar in en input med vilket namn som önskas tas bort från en av listorna
if namn in male: #om namnet är i listan med mansnamn så tas det bort och de uppdaterade listorna skrivs ut
    male.remove(namn)
    print ("Män:", male)
    print ("Kvinnor:", female)
elif namn in female: #om namnet är i listan med flicknamn så tas det bort och de uppdaterade listorna skrivs ut
    female.remove(namn)
    print ("Män:", male )
    print ("Kvinnor:", female) 
else: #om namnet inte finns med i någon av listorna skrivs ett felmeddelande ut
    print("Namnet finns inte med i någon av listorna")