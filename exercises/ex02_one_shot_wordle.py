"""EX01 - One-shot Wordle"""
__author__ = "730391057"

answer: str = "python"
guess: str = input(f"What is your {len(answer)}-letter guess? ")
word_idx: int = 0
box: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(answer):
    guess = input(f"That was not {len(answer)} letters! Try again: ")

while word_idx < len(answer):
    if word_idx < len(guess) and guess[word_idx] == answer[word_idx]:
        box += GREEN_BOX
    else:
        box += WHITE_BOX
    word_idx += 1

print(box)

if guess != answer:
    print("Not quite. Play again soon! ")

if guess == answer:
    print("Woo! You got it! ")

    