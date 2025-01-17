"""EX07 - Testing dicts!"""
__author__ = "730391057"


from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


# use case
def test_invert_use() -> None:
    """Testing if invert return a normal dictionary of letters given another dictionary of letters."""
    dict_1: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(dict_1) == {"z": "a", "y": "b", "x": "c"}


# use case
def test_invert_use_2() -> None:
    """Testing if invert returns a normal dictionary of words given another dictionary of words."""
    dict_1: dict[str, str] = {"apple": "yummy", "chocolate": "delicious", "pizza": "scrumptious", "pasta": "delectable", "candy": "spooky"}
    assert invert(dict_1) == {"yummy": "apple", "delicious": "chocolate", "scrumptious": "pizza", "delectable": "pasta", "spooky": "candy"}


# edge case
def test_invert_edge_case() -> None:
    """Testing if invert returns an empty dictionary when given an empty dictionary."""
    dict_1 = {} 
    assert invert(dict_1) == {}


# optional addition of key error test
def test_invert_key_error() -> None:
    """Testing if invert returns a KeyError when a value is duplicated."""
    with pytest.raises(KeyError):
        dict_1: dict[str, str] = {"alyssa": "byrnes", "adam": "byrnes"}
        invert(dict_1)


# use case
def test_favorite_color_use() -> None:
    """Testing if favorite_color returns a the most popular color given a dictionary of colors."""
    dict_1: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(dict_1) == "blue"


# use case
def test_favorite_color_use_2() -> None:
    """Testing if favorite_color returns the first color when there is a tie of favorite colors."""
    dict_1: dict[str, str] = {"Blair": "pink", "Zoe": "pink", "Caroline": "carolina blue", "Mansi": "carolina blue"}
    assert favorite_color(dict_1) == "pink"


# use case- optional based on gradescope
def test_favorite_color_use_3() -> None:
    """Testing if favorite_color returns the favorite color when everyone has the same favorite color."""
    dict_1: dict[str, str] = {"Blair": "black", "Zoe": "black", "Caroline": "black", "Mansi": "black"}
    assert favorite_color(dict_1) == "black"


# edge case
def test_favorite_color_edge_case() -> None:
    """Test favorite_color function with an empty dictionary."""
    colors_dict: dict[str, str] = {}
    assert favorite_color(colors_dict) == ""


# use case
def test_count_use() -> None: 
    """Testing if a list of strings results in a dict of strings and ints."""
    list_1: list[str] = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    assert count(list_1) == {"apple": 3, "banana": 2, "cherry": 1}


# use case
def test_count_use_2() -> None: 
    """Testing if a list of strings results in a dict of strings and ints (with more inputs)."""
    list_1: list[str] = ["red", "blue", "yellow", "red", "red", "red", "green", "pink", "green"]
    assert count(list_1) == {"red": 4, "blue": 1, "yellow": 1, "green": 2, "pink": 1}


# edge case
def test_count_edge() -> None:
    """Testing if an empty count list results in an empty dict."""
    list_1: list[str] = []
    assert count(list_1) == {}


# use case
def test_alphabetizer_use() -> None:
    """Testing if a list of strings results in a dictionary categorized by letters."""
    list_1: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(list_1) == {"c": ["cat", "car"], "a": ["apple", "angry"], "b": ["boy", "bad"]}


# use case
def test_alphabetizer_use_case_2() -> None:
    """Test alphabetizer function with a list of capitalized country names."""
    list_1: list[str] = ["Canada", "Brazil", "China", "Australia", "Denmark"]
    assert alphabetizer(list_1) == {"c": ["Canada", "China"], "b": ["Brazil"], "a": ["Australia"], "d": ["Denmark"]}


# edge case
def test_alphabetizer_edge_case() -> None:
    """Test alphabetizer function with an empty list."""
    list_1: list[str] = []
    assert alphabetizer(list_1) == {}


# use case
def test_update_attendance_use_case() -> None:
    """Test update_attendance function with an existing day and a new student."""
    attendance_dict: dict[str, list[str]] = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
    day: str = "Monday"
    student: str = "Eve"
    assert update_attendance(attendance_dict, day, student) == {"Monday": ["Alice", "Bob", "Eve"], "Tuesday": ["Charlie"]}


# use case
def test_update_attendance_use_case_2() -> None:
    """Test update_attendance function with a new day and a new student."""
    attendance_dict: dict[str, list[str]] = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
    day: str = "Wednesday"
    student: str = "Frank"
    assert update_attendance(attendance_dict, day, student) == {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"], "Wednesday": ["Frank"]}


# edge case
def test_update_attendance_edge_case() -> None:
    """Test update_attendance function with the addition of a student's name that is already in there."""
    attendance_dict: dict[str, list[str]] = {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}
    day: str = "Monday"
    student: str = "Alice"
    assert update_attendance(attendance_dict, day, student) == {"Monday": ["Alice", "Bob"], "Tuesday": ["Charlie"]}