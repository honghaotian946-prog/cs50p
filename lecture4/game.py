#Guessing Game
import random
import sys

while True:
    try:
        level = input("Level:")
        if level.isdigit() == False or int(level)<=1:
            raise ValueError
    except ValueError:
        pass
    else:
        break

real = random.randint(1,int(level))

while True:
    guess = int(input("Guess:"))
    try:        
        if guess<1:
            raise ValueError
        if guess > real:
            print("Too large!")
        elif guess < real:
            print("Too small!")
        else:
            sys.exit("Just right")
    except ValueError:
        pass