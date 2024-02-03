""""Number guessing game."""
from random import randint 

SECRET: int = randint(1,10)
correct: bool = False

while correct == False: #not correct
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True 
    elif guess < 0: 
        print("Too low!")
        print("Try Again!")
    elif guess > 10: 
        print("Too high!")
        print("Try Again!")
    