"""EX01 - Dict exercise!"""
__author__ = "730391057"

def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values."""
    inverted_dict = {}
    
    for key, value in input_dict:
        # Check if the value is already in the inverted dictionary
        if value in inverted_dict:
            # If the value is already a key in the inverted dictionary, raise a KeyError
            raise KeyError(f"KeyError: Duplicate value '{value}' encountered.")
        else:
            # Otherwise, add the inverted key-value pair to the inverted dictionary
            inverted_dict[value] = key
    
    return inverted_dict

# FIXXXXXX!
def favorite_color(color_dict: dict[str, str]) -> str:
    color_count = {}  # Dictionary to store color counts
    most_popular_color: str = ""
    max_count: int = 0

    for color in color_dict:
        if color not in color_count:
            color_count[color] = 1
        else:
            color_count[color] += 1

        # Update the most popular color
        if color_count[color] > max_count:
            max_count = color_count[color]
            most_popular_color = color

    return most_popular_color


def count(input_list: list[str]) -> dict[str, int]:
    count_dict = {}  # Initialize an empty dictionary to store the counts
    
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1  # Increment the count if the item is already in the dictionary
        else:
            count_dict[item] = 1  # Initialize the count to 1 for a new item
    
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    alphabet_dict = {}  # Initialize an empty dictionary to store the categorized words
    
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
    # Check if the day already exists in the dictionary
    if day in attendance_dict:
        # If the day exists, append the student to the list of attendees for that day
        attendance_dict[day].append(student)
    else:
        # If the day does not exist, create a new entry with the day as the key and a list containing the student
        attendance_dict[day] = [student]
    
    return attendance_dict


if __name__ == "__main__":
    # Example usage and testing
    color_dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    result = favorite_color(color_dict)
    print(result)