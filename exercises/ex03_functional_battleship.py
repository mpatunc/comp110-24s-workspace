"""EX03 - Function Battleship."""

__author__ = "730602218"
import random


# input for grid size and column or row! 
def input_guess(grid_size: int, row_or_column: str) -> int: 
    """Function for guesses."""
    # player can choose row or column 
    assert row_or_column == "row" or row_or_column == "column"  
    guess: int = 0 
    if row_or_column == "row": 
        guess = int(input("Guess a row: "))
    else: 
        guess = int(input("Guess a column: "))
    while guess < 1 or guess > grid_size: 
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess 


# grid making 
# emoji codes 
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
guess_box: str = "\U0001F7E6"  


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct_guess: bool) -> None:
    """Function for printing grid."""
    # if row_guess == correct_guess and column_guess == correct_guess: 
    #     guess_box = RED_BOX
    # else: 
    #     guess_box = WHITE_BOX # not working for some reason
    # making sure true is red and while is false 
    if correct_guess: 
        guess_box = RED_BOX
    else:
        guess_box = WHITE_BOX
    # code from EXO2 for grid anatomy
    r_counter: int = 1    
    while r_counter <= grid_size:
        row_em: str = ""
        c_counter: int = 1
        if row_guess == r_counter: 
            while c_counter <= grid_size:
                if column_guess == c_counter:
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

# correct guess function


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Function for correct guess."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False

# main function 


def main(grid_size: int, secret_row: int, secret_column: int) -> None: 
    """Main function."""
    turn_guess: int = 1
    win: bool = False
    while turn_guess <= 5 and not win: 
        print(f"=== Turn {turn_guess}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        # call correct guess 
        correct: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)
        # call for print grid 
        print_grid(grid_size, row_guess, column_guess, correct)
        # correct or incorrect
        if correct:
            print("Hit!")
            print(f"You won in {turn_guess}/5 turns!")
            turn_guess += 5 
        else: 
            print("Miss!")
            if turn_guess == 5:
                print("X/5 - Better luck next time!")
        turn_guess += 1
        
        
if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))