"""The file where I import stuff"""

from lessons import my_functions
from lessons.my_functions import double, double_display

# # __name__ = "__main__":
print(my_functions.add(4,5))
# # will also print out stuff in another module calling 
# #the same function unless made into comment


# print(double(1))
# double_display(4)