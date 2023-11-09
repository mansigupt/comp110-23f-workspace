"""File to define Fish class."""
__author__ = "730391057"


class Fish:
    """Defining class Fish that will be used in river simulation."""
    def __init__(self):
        """Constructor for fish class."""
        self.age = 0
        return None
    
    def one_day(self):
        """Function for hunger and age after one day."""
        self.age += 1
        return None