"""Practicing Counters"""

num_string: str = "203"

number_of_odds: int = 0

if int(num_string[0]) % 2 == 1: 
    number_of_odds = number_of_odds + 1

if int(num_string[1]) % 2 == 1: 
    number_of_odds = number_of_odds + 1

if int(num_string[2]) % 2 == 1: 
    number_of_odds = number_of_odds + 1



print(number_of_odds)