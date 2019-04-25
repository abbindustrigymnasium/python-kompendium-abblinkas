mängd = range(500)
summa = 0

for i in mängd:
        i += 1
        if i%2 != 0:
                summa += i

print(summa)