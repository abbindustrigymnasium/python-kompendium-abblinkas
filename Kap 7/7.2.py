import random #importerar biblioteket random

count = 0
number = random.randint(1,100) #ett random nummer mellan 1 och 100

print(".: THE HIGHER LOWER GAME :.")
print("---------------------------")
print("Welcome to The Higher Lower\nGame. I will randomise a\nnumber between 0 and 99.\nCan you guess it?")
while True: #körs till programmet breakas
    guess = int(input("Your guess ")) #tar in en input på användarens gissning
    if guess == number: #om användaren gissar rätt
        print(str(guess) + "is correct!\nIt took you " + str(count) + " guesses.\nGood job!") #skrivs ett meddelande ut att man gissat rätt och på hur många försök
        break #programmet stängs av
    elif guess < number: #annars om gissningen är lägre än numret
        print("HIGHER!")
        count +=1 #lägger man till 1 gissning i minne
        continue #fortsätter programmet
    elif guess > number: #om gissningen är högre än numret
        print("LOWER!")
        count +=1 #lägger man till 1 gissning i minne
        continue #om gissningen är högre än numret