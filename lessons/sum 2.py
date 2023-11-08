"""Summing the elements of a list using different loops."""
__author__ = "730391057"


def w_sum(vals: list[float]) -> float:
    """Going through each index and adding it together with a while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    
    return sum


def f_sum(vals: list[float]) -> float:
    """Going through each index and adding it together with a for...in... loop."""
    add: float = 0.0
    for num in vals:
        add += num
    
    return add


def f_range_sum(vals: list[float]) -> float:
    """Going through each index and adding it together with a for...inrange... loop."""
    sum_add: float = 0.0
    for index in range(len(vals)):
        sum_add += vals[index]
    
    return sum_add