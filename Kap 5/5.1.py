Daniel_Radcliffe = ["man", "brun", "brun", "Daniel Radcliffe"]
Rupert_Grint = ["man", "röd", "blå", "Rupert Grint"]
Emma_Watson = ["kvinna", "brun", "brun", "Emma Watson"]
Selena_Gomez = ["kvinna", "brun", "brun", "Selena Gomez"]
Linus_Kasper = ["man", "blond", "brun", "Linus Kasper"]
Lindrit_Koxha = ["man", "brun", "brun", "Lindrit Koxha"]
kändisar = [Daniel_Radcliffe, Rupert_Grint, Emma_Watson, Selena_Gomez, Linus_Kasper, Lindrit_Koxha]
lookalikes = ""

print("Ange kön:")
kön = str(input())
print("Ange hårfärg:")
hårfärg = str(input())
print("Ange ögonfärg:")
ögonfärg = str(input())

for personer in kändisar:
    if personer[0] == kön:
        if personer[1] == hårfärg:
            if personer[2] == ögonfärg:
                lookalikes += personer[3] + ", "
if lookalikes == "":
    print("Du liknar dessvärre ingen kändis...")
else:
    print("Du liknar " + lookalikes + "!")