"""Defining a class!"""

from __future__ import annotations

"""
Think of a class definition as a "roadmap" for objects 
that belong to the class. You are deining the 
underlying structure every instance of this class will have.
"""

class Pizza: 

    # attributes
    # Think of these as the variables each instance of my class will have.
    # <name>: <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        """My constructor"""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gf = inp_gf
        # returns a Pizza object

    def price(self) -> float:
        """Calculate the price of pizza"""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gf:
            price += 1.00
        return price
    
    def add_toppings(self, num_toppings: int) -> None:
        """Add toppings to existing pizza"""
        self.toppings += num_toppings

    def make_new_pizza_and_add_new_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizza's properties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gf)
        return new_pizza
    
    def __str__(self) -> str:
        pizza_info: str = f"PIZZA ORDER: size {self.size}, toppings: {self.toppings}, gf: {self.gf}"
        return pizza_info

my_pizza: Pizza = Pizza("medium", 3, False)
print(str(my_pizza))
sals_pizza: Pizza = Pizza("large", 1, True)
print(sals_pizza)
