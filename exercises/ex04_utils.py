"""EX04 - List Utils!"""
__author__ = "730391057"


def all(int_list: list[int], target_int: int) -> bool:
    """All the ints in the list are the same as the target int."""
    # If the list is empty return False
    if not int_list: 
        return False
    
    # While the index of int list is less than the total length of list, check if the int matches
    int_idx: int = 0
    while int_idx < len(int_list):
        if int_list[int_idx] != target_int:
            return False
        int_idx += 1
    
    # True if all integers in the list are equal to the target integer, False otherwise.
    return True


def max(input: list[int]) -> int:
    """Return the largest number in a list."""
    # If the length of the list is 0, then produce error message saying list is empty
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_num: int = input[0]
    num_idx: int = 0

    # While the index of the num is less than the length of the list check to see if the number is larger.
    # If the number is larger change the variable to the new number in the list
    while num_idx < len(input):
        if input[num_idx] > max_num:
            max_num = input[num_idx]
        num_idx += 1
    
    return max_num


def is_equal(list1: str, list2: str) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    idx1: int = 0
    idx2: int = 0

    # While loop to check is if the indexes in two different lists are equal
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] != list2[idx2]:
            return False
        idx1 += 1
        idx2 += 1
    
    # Returns false is the length of the two lists are different
    if idx1 < len(list1) or idx2 < len(list2):
        return False

    # True if every element at every index is equal in both lists, False otherwise.
    return True
