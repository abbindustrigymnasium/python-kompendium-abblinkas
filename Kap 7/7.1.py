multitab = int(input("Ange en multiplikationstabell"))
number = 0
numberoftimes = 3
tot= multitab

while True:
    print(tot)
    tot += multitab
    number += 1
    if number == numberoftimes:
        answer = str(input("Fortsätt? "))
        if answer.lower() == "ja":
            numberoftimes +=3
            continue
        elif answer.lower() == "nej":
            break
        else:
            break