""""Example functions to learn definition and calling syntax"""

# function to choose a maximum out of to numbers 
def my_max(number1: int, number2: int) -> int:
    """returns the maximum value out of two numbers"""
    if number1 >= number2: 
        # return tells us what value is given back or what function output is.
        return number1 
    else: # number one is less than number two 
        return number2

# returns do not print, so you need to make an variable and then 
# print that variable 
max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
print (max_number)

# need to define function first then call it or else it won't work


