"""Return a new list containing the elements of a list that are odd with an even index."""
__author__ = "730391057"

def odd_and_even(nums: list[int]) -> list[int]:
    """This function should return a list of odd numbers at even indicies."""
    odd_nums: list[int] = []
    for i in range(0, len(nums)):
        if nums[i] % 2 != 0 and i % 2 == 0:
            odd_nums.append(nums[i])
    
    return odd_nums