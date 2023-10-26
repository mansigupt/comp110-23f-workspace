"""Combining two lists into a dictionary!"""
__author__ = "730391057"


def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    """Produce a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    if len(list_1) != len(list_2):
        return dict()
    if len(list_1) == 0 or len(list_2) == 0:
        return dict()
    new_dict: dict[str, int] = {}

    idx: int = 0
    while idx < len(list_1):
        new_dict[list_1[idx]] = list_2[idx]
        idx += 1
    
    return new_dict