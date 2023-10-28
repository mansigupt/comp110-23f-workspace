"""EX06 - Dict practice exercise!"""
__author__ = "730391057"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str,str] that inverts the keys and the values."""
    inverted_dict: dict[str, str] = {}
    
    for key in input_dict:  # Iterate over keys in the input dictionary.
        value = input_dict[key]  # Get the value for the current key.
        
        # Check if the value is already in the inverted dictionary
        if value in inverted_dict:
            # If the value is already a key in the inverted dictionary, raise a KeyError
            raise KeyError(f"KeyError: Duplicate value '{value}' encountered.")
        else:
            # Otherwise, add the inverted key-value pair to the inverted dictionary
            inverted_dict[value] = key
    
    return inverted_dict


def favorite_color(colors_dict: dict[str, str]) -> str:
    """Return the most popular color in a dictionary and if it's a tie return the first color in the dict."""
    color_count: dict[str, int] = {}  # Initialize an empty dict to count occurrences of each color
    # Initialize variables to keep track of the most popular color and its count.
    most_popular_color: str = "" 
    max_count: int = 0

    # Iterate through the values in colors_dict.
    for color in colors_dict.values():
        if color in color_count:  # Check if the color is already in the color_count dictionary.
            color_count[color] += 1  # Add the count for the current color if present.
        else:
            color_count[color] = 1  # If the color is not in the dictionary, add it with a count of 1.

        # If the count for the current color is greater than the max count, update the most_popular_color.
        if color_count[color] > max_count:
            max_count = color_count[color]
            most_popular_color = color
        # If there's a tie in count, check the order of appearance and select the first color.
        elif color_count[color] == max_count:
            if list(colors_dict.values()).index(color) < list(colors_dict.values()).index(most_popular_color):
                most_popular_color = color

    return most_popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """Count the occurrences of each item in the input list and return a dictionary of counts."""
    count_dict: dict[str, int] = {}  # Initialize an empty dictionary to store the counts
    
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1  # Increase the count if the item is already in the dictionary
        else:
            count_dict[item] = 1  # Initialize the count to 1 for a new item
    
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Categorize words from the list based on their first letter."""
    alphabet_dict: dict[str, list[str]] = {}  # Initialize an empty dictionary to store the categorized words
    
    for word in word_list:
        first_letter = word[0].lower()  # Get the lowercase first letter of the word
        
        if first_letter in alphabet_dict:
            # If the letter is already a key, append the word to the existing list
            alphabet_dict[first_letter].append(word)
        else:
            # If the letter is not a key, create a new list with the word
            alphabet_dict[first_letter] = [word]
    
    return alphabet_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Update the attendance dictionary by adding a student to a specific day's attendance list."""
    # Check if the day already exists in the dictionary
    if day in attendance_dict:
        # If the day exists, append the student to the list of attendees for that day
        attendance_dict[day].append(student)
    else:
        # If the day does not exist, create a new entry with the day as the key and a list containing the student
        attendance_dict[day] = [student]
    
    return attendance_dict
