"""File to define River class."""
__author__ = "730391057"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

day: int
bears: list[Bear]
fish: list[Fish]


class River:
    """Defining class River that will be used in river simulation."""
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Defining a function that as animal’s age, they sare removed from the River."""
        new_bears = []
        new_fish = []

        # Iterate through the Bears and check their ages
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)

        # Iterate through the Fish and check their ages
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)

        # Update self.bears and self.fish with the new lists
        self.bears = new_bears
        self.fish = new_fish
        return None

    def remove_fish(self, amount: int):
        """Function to remove frontmost fish from the River."""
        # Remove the frontmost Fish (Fish at index 0) 'amount' times using a while loop
        while amount > 0:
            self.fish.pop(0)
            amount -= 1

    def bears_eating(self):
        """Function so that for each Bear, if there are at least 5 Fish in the river, the Bear will eat 3 Fish."""
        if len(self.fish) >= 5:
            # Iterate through the Bears
            for bear in self.bears:
                # Ensure there are still at least 5 Fish in the river before eating
                if len(self.fish) >= 5:
                    # Remove 3 Fish from the river
                    self.remove_fish(3)
                    # Call the eat method for the Bear to update its hunger_score
                    bear.eat(3)
        return None
    
    def check_hunger(self):
        """Function to check the hunger_score of every Bear in the river. If hunger_score < 0, then remove the Bear from the river."""
        new_bears = []
    
        # Iterate through the Bears and check their hunger_score
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)

        # Update self.bears with the new list containing only surviving Bears
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Function so that each pair of fish will produce 4 offspring."""
        num_fish = len(self.fish)
        num_new_fish = (num_fish // 2) * 4

    # Add num_new_fish new Fish instances to the fish list using a while loop
        while num_new_fish > 0:
            self.fish.append(Fish())
            num_new_fish -= 1
    
        return None
    
    def repopulate_bears(self):
        """Function so that each pair of Bear’s will produce 1 offspring."""
        num_bears = len(self.bears)
        num_new_bears = num_bears // 2

        # Add num_new_bears new Bear instances to the bears list 
        while num_new_bears > 0:
            self.bears.append(Bear())
            num_new_bears -= 1
    
        return None
    
    def view_river(self):
        """Function to print the river status out."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Function to call one_river_day() seven times.""" 
        days: int = 0
        while days < 7:
            self.one_river_day()
            days += 1