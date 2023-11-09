"""File to define Bear class."""
__author__ = "730391057"


class Bear:
    """Defining class Bear that will be used in river simulation."""
    def __init__(self):
        """Constructor for bear class."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Function for hunger and age after one day."""
        self.hunger_score -= 1
        self.age += 1
        return None
    
    def eat(self, num_fish: int):
        """Function to update the bear's hunger score."""
        self.hunger_score += num_fish