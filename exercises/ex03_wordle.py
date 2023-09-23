"""EX03 - Structured Wordle!"""
__author__ = "730391057"

def contains_char(search_word: str, find_char: str)-> bool:
    """Determining if a single character is part of the word."""
    assert len(find_char) == 1
    word_idx: int = 0
    while word_idx < len(search_word):
        if search_word[word_idx] == find_char:
            return True
        word_idx += 1
    
    return False  

def emojified(guess: str, secret: str)-> str:
    """Create an emoji code to suggest if letters are in the correct positions"""
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji = ""
    emoji_idx: int = 0

    while emoji_idx < len(guess):
        if guess[emoji_idx] == secret[emoji_idx]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[emoji_idx]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        emoji_idx += 1

    return emoji

def input_guess(expected_length: int)-> str:
    """Prompt the user for a guess of the expected length and continue prompting until a valid guess is provided."""
    user_guess = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess= input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "hello"
    max_tries: int = 6
    current_try: int = 1
    while current_try <= max_tries:
        print(f"=== Turn {current_try}/{max_tries} ===")
    
