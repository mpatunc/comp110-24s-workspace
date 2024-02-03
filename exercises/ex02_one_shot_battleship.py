"""EX02 - One Shot Battleship."""

__author__ = "730602218"

grid_size: int = 4 
secret_row: int = 3
secret_column: int = 2
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
guess_box: str = "\U0001F7E6"

# Row guess and Column guess 
player_guess_row: int = int(input("Guess a row: "))

while player_guess_row > grid_size or player_guess_row <= 0:
    player_guess_row = int(input("The grid is only 4 by 4. Try again: "))

player_guess_column: int = int(input("Guess a column: "))

while player_guess_column > grid_size or player_guess_column <= 0:
    player_guess_column = int(input("The grid is only 4 by 4. Try again: "))

# If correct change guess box to red, if not change to white 
if secret_row == player_guess_row and secret_column == player_guess_column:
    guess_box = RED_BOX
else: 
    guess_box = WHITE_BOX

# Gird layout 
r_counter: int = 1 
while r_counter <= grid_size:
    row_em: str = ""
    c_counter: int = 1
    if player_guess_row == r_counter: 
        while c_counter <= grid_size:
            if player_guess_column == c_counter:
                row_em += guess_box
            else: 
                row_em += BLUE_BOX
            c_counter += 1
    else:
        while c_counter <= grid_size:
            row_em += BLUE_BOX
            c_counter += 1
    print(row_em)
    r_counter += 1 

# Hit Miss or Hint 
if secret_row == player_guess_row and secret_column == player_guess_column:
    print("Hit!")
elif player_guess_row == secret_row:
    player_guess_column != secret_column
    print("Close! Correct row, wrong column.")
elif player_guess_column == secret_column:
    player_guess_row != secret_row
    print("Close! Correct column, wrong row.")
else: 
    print("Miss!")