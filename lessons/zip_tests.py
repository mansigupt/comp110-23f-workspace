"""Test my zip function!"""
__author__ = "730391057"

from lessons.zip import zip


# edge case
def test_zip_diff_length():
    """Testing if zip return an empty dictionary if list are different lengths."""
    list_1: list[str] = ["apple", "banana", "cherry"]
    list_2: list[int] = [1, 2]
    assert zip(list_1, list_2) == {}


# use case
def test_zip_normal():
    """Testing if zip return an a normal dictionary given two lists of the same length."""
    test_list_1: list[str] = ["Happy", "Tuesday"]
    test_list_2: list[int] = [1, 2]
    assert zip(test_list_1, test_list_2) == {"Happy": 1, "Tuesday": 2}


# use case
def test_zip_normal_2():
    """Testing if zip return an a normal dictionary given two lists of the same length, but longer lists and numbers rearranged."""
    test_list_1: list[str] = ["I", "love", "comp", "110"]
    test_list_2: list[int] = [1, 3, 4, 2]
    assert zip(test_list_1, test_list_2) == {"I": 1, "love": 3, "comp": 4, "110": 2}