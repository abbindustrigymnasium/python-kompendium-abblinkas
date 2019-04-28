förnamn=["Maria", "Erik", "Karl"] #lista med registrerade namn
efternamn=["Svensson", "Karlsson", "Andersson"] #lista med avanmälda namn

for firstname in förnamn: #för varje plats i listan förnamn
    for lastname in efternamn: #för varje plats i listan efternamn
        print(firstname + " " + lastname) #skriver ut det sammansatta namnet
#eftersom man kollar varje förnamn och efternamn och skriver ut de så kommer alla olika varianter av namn skrivas ut