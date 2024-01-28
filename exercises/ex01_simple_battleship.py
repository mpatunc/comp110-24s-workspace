"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730602218"

player_1_str: str = input("Pick a secret boat location between 1 and 4: ")
player_1: int = int(player_1_str)

if player_1 >= 5: 
    print("Error! 5 too high!")
    exit()
if player_1 <= 0: 
    print("Error! 0 too low!")
    exit()

player_2_guess_str: str = input("Guess a number between 1 and 4: ")
player_2_guess: int = int(player_2_guess_str)
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
guess_box: str = "\U0001F7E6"

if player_2_guess >= 5:
    print("Error! 5 too high!")
    exit()
if player_2_guess <= 0: 
    print("Error! 0 too low!")
    exit()

if player_1 == player_2_guess:
    guess_box = RED_BOX
else: 
    guess_box = WHITE_BOX

if player_2_guess == 1: 
    print(guess_box + BLUE_BOX + BLUE_BOX + BLUE_BOX)

if player_2_guess == 2: 
    print(BLUE_BOX + guess_box + BLUE_BOX + BLUE_BOX)

if player_2_guess == 3: 
    print(BLUE_BOX + BLUE_BOX + guess_box + BLUE_BOX)

if player_2_guess == 4: 
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + guess_box)

if player_1 == player_2_guess:
    print("Correct! You hit the ship!")
else: 
    print("Incorrect! You missed the ship!")