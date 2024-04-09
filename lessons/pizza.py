"""Define Pizza class."""

class Pizza: 

    # attributes: 
    size: str # "small" or "large"
    toppings: int
    gluten_free: bool # True if GF False if not

    def __init__(self, size_inp: str, toppings_inp: int, gluten_free_inp: bool):
        self.size = size_inp
        self.toppings = toppings_inp
        self.gluten_free = gluten_free_inp
        # it actually returns self

    def price(self) -> float: 
        """Calculate and return price of pizza."""
        cost: float = 0.0
        if self.size == "large":
            cost = 6.0
        else: 
            cost = 5.0
        # toppings cost 75 cents per topping 
        cost += 0.75 * self.toppings
        # if gluten free add 1 dollar 
        if self.gluten_free: 
            cost += 1 
        return cost
    
    def add_toppings(self, num_toppings: int) -> None: 
        """Add toppings."""
        self.toppings += num_toppings