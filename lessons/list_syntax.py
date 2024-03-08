"""Lists Syntax"""

# Initialize an empty list 
grocery_list: list[str] = list() # <- list constructor 
grocery_list: list[str] = [] # <- literal (nothing in it just empty list)

# Adding an item to a list 
# append adds things to the end of the lists 
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# Create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list: ")
print(grocery_list2)

# Indexing 
print("Print first element of string: ")
print(grocery_list[0])

# Modifying by index 
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print(grocery_list)

# Measuring length
print("Length of list: ")
print(len(grocery_list))

# Remove an item from a list 
grocery_list.pop(1)
print("After removing almond milk: ")
print(grocery_list)

# Function name: display 
# Parameter: list[str]
# Return nothing 
# Print out list

def display(word: list[str]) -> None:
    print(word) 

display(grocery_list) 

# Create a list 
# Name: create
# parameters: str and str 
# rv list[str]
# put both parameters into list and return that list 

def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list

print(create("Hello", "World"))

