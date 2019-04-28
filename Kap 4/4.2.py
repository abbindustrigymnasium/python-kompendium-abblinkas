mängd = range(500)#skapar en lista med tal från 0 -499
summa = 0
 
for i in mängd: #för varje tal i listan mängd
        i += 1 #adderar 1 eftersom listan startar på 0
        if i%2 != 0: #om talet delar på 2 inte har någon rest(talet är ojämnt)
                summa += i #adderar talet till summan

print(summa) #skriver ut summan av alla ojämna tal från 1-500 adderade med varandra