from __future__ import annotations

def free_biscuits(basketball_dict: dict[str, list[int]]) -> dict[str, bool]:
    """Checks which games get free biscuits!"""
    free_points: dict[str, bool] = {} 
    for game in basketball_dict:
        # sum up the values in the list
        points: int = 0
        for num in basketball_dict[game]:
            points += num
        if points >= 100:
            free_points[game] = True
        else:
            free_points[game] = False

    return free_points


def max_key(num_dict: dict[str, list[int]]) -> str:
    """Returns string with the highest sum."""
    highest_key: str = ""
    max_sum: int = 0
    for str in num_dict:
        total: int = 0
        for num in num_dict[str]:
            total += num
        if total > max_sum:
            max_sum = total
            highest_key = str

    return highest_key

# Recursion example
def multiples(num_list: list[int]) -> list[bool]:
    multiple: list[bool] = []
    for idx in range(0,len(num_list)):
        if idx == 0:
            multiple.append(num_list[idx] % num_list[len(num_list) - 1] == 0)
        else:
            multiple.append(num_list[idx] % num_list[idx - 1] == 0)

    return multiple

def merge_lists(words: list[str], nums: list[int]) -> dict[str, int]:
    combined: dict[str, int] = {}
    if len(words) != len(nums):
        return combined
    
    for idx in range(0,len(words)):
        combined[words[idx]] = nums[idx]
    
    return combined

def reverse_multiply(nums: list[int]) -> list[int]:
    new_list: list[int] = []
    i: int = len(nums) - 1
    while i >= 0:
        new_list.append(nums[i] * 2)
        i -= 1
    return new_list 

class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int) -> None:
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int):
        self.marshmallow_count += mallows
        self.sweetness += mallows * 2

    def calorie_count(self) -> float:
        calories: float = 0

        if self.flavor == "vanilla" or self.flavor == "peppermint":
            calories += 30
        else:
            calories += 20

        if self.has_whip == True:
            calories += 100
        
        calories += self.marshmallow_count / 2

        return calories
    

class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, time: int) -> None:
        self.minutes += time

    def reset(self) -> int:
        num: int = self.minutes
        self.minutes = 0
        return num

    def report(self) -> None:
        mins: int = self.minutes % 60
        hours: int = self.minutes // 60
        print (f"{self.name} has spent {hours} hours and {mins} minutes on {self.purpose}.")

class Piggies:

    oink: bool
    name: str
    age: int

    def __init__(self, oink: bool, name: str, age: int):
        self.oink = oink
        self.name = name
        self.age = age

    def __add__(self, years: int) -> Piggies:
        new_pig: Piggies = Piggies(self.oink, self.name, self.age + years)
        return new_pig
    
    def rename(self, new_name: str):
        self.name = new_name
        
pig1: Piggies = Piggies(True, "Wilbur", 1)
pig2: Piggies = pig1 + 2
pig2.age
print(pig2.name)
pig2.rename("Babe")
print(pig2.name)
        