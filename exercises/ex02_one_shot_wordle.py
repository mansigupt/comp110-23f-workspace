"""EX01 - One-shot Wordle!"""
__author__ = "730391057"

answer: str = "python"
guess: str = input(f"What is your {len(answer)}-letter guess? ")
word_idx: int = 0
box: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Ensure the guessed word has the same length as the answer
while len(guess) != len(answer):
    guess = input(f"That was not {len(answer)} letters! Try again: ")

while word_idx < len(answer):
    if word_idx < len(guess) and guess[word_idx] == answer[word_idx]:
        # Insert green box for correct character and position
        box += GREEN_BOX
    else:
        # Initialize boolean and alternate index variables
        diff_place = False
        alt_index: int = 0
        # While loop to check for matches elsewhere in the secret word
        while not diff_place and alt_index < len(answer):
            if alt_index != word_idx and guess[word_idx] == answer[alt_index]:
                diff_place = True
            alt_index += 1
        if diff_place:
            # Add a yellow box for correct character but wrong position
            box += YELLOW_BOX
        else: 
            # Add a white box for incorrect character
            box += WHITE_BOX
    word_idx += 1

print(box)

if guess != answer:
    print("Not quite. Play again soon! ")

if guess == answer:
    print("Woo! You got it! ")

    