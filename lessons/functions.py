"""Demonstrates functions"""
from random import randint
# this function needs to be imported so we can use it

print("Hello!")

# round function needs to have print in front of it because a function 
# returns something not print something

print(round(10.25))

# or 

x: int = round(10.25)
print(x) 

# Need to give randint a range 
z: int = randint(1,7)
print(z)
