"""Practice instantiating Pizza class."""

from lessons.pizza import Pizza

# instantiation
my_pizza: Pizza = Pizza("large", 1, True) # with _init_ : Pizza("large", 1, True)
# my_pizza.size = "large" # once add __init__ then dont need this part of function
# my_pizza.toppings = 1
# my_pizza.gluten_free = True

sals_pizza: Pizza = Pizza("small", 2, False)

# print(Pizza)
# print(my_pizza)
# print(my_pizza.size)

# def price(pizza_order: Pizza) -> float: 
#     """Calculate and return price of pizza."""
#     cost: float = 0.0
#     if pizza_order.size == "large":
#         cost = 6.0
#     else: 
#         cost = 5.0
#     # toppings cost 75 cents per topping 
#     cost += 0.75 * pizza_order.toppings
#     # if gluten free add 1 dollar 
#     if pizza_order.gluten_free: 
#         cost += 1 
#     return cost

print(my_pizza.toppings)
print(my_pizza.price())
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())