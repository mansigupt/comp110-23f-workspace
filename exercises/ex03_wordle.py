"""EX03 - Structured Wordle!"""
__author__ = "730391057"


def contains_char(search_word: str, find_char: str) -> bool:
    """Determining if a single character is part of the word."""
    assert len(find_char) == 1  # Making sure find_char is actually one character
    word_idx: int = 0
    while word_idx < len(search_word):  # While the index of the word is less than the total length of word
        if search_word[word_idx] == find_char:  # If the index of word given is the same as the character, then print True
            return True
        word_idx += 1
    
    return False  # Otherwise, if they are not the same print False


def emojified(guess: str, secret: str) -> str:
    """Create an emoji code to suggest if letters are in the correct positions."""
    assert len(guess) == len(secret)
    # Variables for emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # Similar to EX02, create an empty string and another index
    emoji = ""
    emoji_idx: int = 0
    # While the index of the emoji is less than the total length of the guess...
    while emoji_idx < len(guess):
        if guess[emoji_idx] == secret[emoji_idx]:  # If a certain index of the guess is equal to the secret in the same position, print a green box
            emoji += GREEN_BOX
        elif contains_char(secret, guess[emoji_idx]):  # If a certain index of the guess is not in the same position as the secret but still contained in the word, print a yellow box
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX  # If a certain index of the guess is not even present in the secret word, print a white box
        emoji_idx += 1

    return emoji  # Telling it to print the emojis after going through the while function


def input_guess(expected_length: int) -> str:
    """Prompt the user for a guess of the expected length and continue prompting until a valid guess is provided."""
    user_guess = input(f"Enter a {expected_length} character word: ")  # Asking the user to enter a guess of a certain length
    while len(user_guess) != expected_length:  # If the length of the guess is not equal to the length expected then print the next line
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess  # If the lengths are the same, then print the guess of the correct length in the next line


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    max_tries: int = 6
    current_try: int = 1
    lost: bool = False  # Set a bool to use throughout the code
    while current_try <= max_tries and not lost:  # While the current try is less than or equal to the max number of tries and is True 
        print(f"=== Turn {current_try}/{max_tries} ===")  # Printing the number of tries used
    
        guess = input_guess(len(secret_word))  # Calling the input_guess function asking the user to guess a word

        emoji = emojified(guess, secret_word)  # Calling the emojified function to print the emojis of the guessed word
        print(emoji)

        if guess == secret_word:  # If the guess is the same as the secret word, change the bool to True
            lost = True
        
        current_try += 1  # Adding the index to continue going through the while loop

    if lost:
        print(f"You won in {current_try - 1}/{max_tries} turns!")  # If the bool was changed to True during the while loop, print that they won
    else:
        print(f"X/{max_tries} - Sorry, try again tomorrow!")  # If they continue through all 6 tries and did not guess the word print the sorry statement


if __name__ == "__main__":
    main()
