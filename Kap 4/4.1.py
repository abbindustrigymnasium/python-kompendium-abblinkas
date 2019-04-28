mängd = range(1000000) #skapar en lista med tal från 0-999999
summa = 0 

for i in mängd: #för varje tal i listan mängd
    i += 1 #adderar 1 eftersom listan startar på 0
    summa += i #adderar talet till summan

print(summa) #skriver ut summan av alla tal från 1-1000000 adderade med varandra