import random

count = 0
number = random.randint(1,100)

print(".: THE HIGHER LOWER GAME :.")
print("---------------------------")
print("Welcome to The Higher Lower\nGame. I will randomise a\nnumber between 0 and 99.\nCan you guess it?")
print(number)
while True:
    guess = int(input("Your guess "))
    if guess == number:
        print(str(guess) + "is correct!\nIt took you " + str(count) + " guesses.\nGood job!")
        break
    elif guess < number:
        print("HIGHER!")
        count +=1
        continue
    elif guess > number:
        print("LOWER!")
        count +=1
        continue