"""Return a boolean of the integer is in the dictionary."""
__author__ = "730391057"

def value_exists(dict1: dict[str,int], value: int) -> bool:
    """Testing if a value exists in a dict"""
    exists: bool = False
    for elem in dict1:
        if dict1[elem] == value:
            exists = True
    
    return exists
