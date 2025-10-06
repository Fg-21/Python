import random

finded = False
number = random.randint(0, 101)
guess = 0


while not finded and guess != -1:
    guess = int(input ("Adivina el numero"))
    if guess < number:
        print("Mayor")
    elif guess > number:
        print("Menor")
    else:
        finded = True
        print ("Acertaste")
    
    