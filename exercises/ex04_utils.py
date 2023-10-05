"""EX04 - List Utils!"""
__author__ = "730391057"


def all(int_list: int, target_int: int) -> bool:
    """All the ints in the list are the same as the target int."""
    if not int_list:
        return False
    
    int_idx: int = 0
    while int_idx < len(int_list):
        if int_list[int_idx] != target_int:
            return False
        int_idx += 1
    
    return True


def max(input: list[int]) -> int:
    """Return the largest number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_num: int = input[0]
    num_idx: int = 0

    while num_idx < len(input):
        if input[num_idx] > max_num:
            max_num = input[num_idx]
        num_idx += 1
    
    return max_num


def is_equal(list1, list2) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    idx1: int = 0
    idx2: int = 0

    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] != list2[idx2]:
            return False
        idx1 += 1
        idx2 += 1
    
    if idx1 < len(list1) or idx2 < len(list2):
        return False

    return True
