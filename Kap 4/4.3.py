registrerade = ["Anna", "Eva", "Erik", "Lars", "Karl"] #lista med registrerade namn
avanmälningar =["Anna", "Erik", "Karl",] #lista med avanmälda namn

for namn in avanmälningar: #för varje plats i avanmälningar
    if namn in registrerade: #kollar om namnet finns i listan för registrerade 
        registrerade.remove(namn) #tar sedan bort namnet från registrerade

print(registrerade) #skriver ut de kvarstående registrerade