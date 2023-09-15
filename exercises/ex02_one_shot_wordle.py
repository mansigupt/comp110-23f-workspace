"""EX01 - One-shot Wordle"""
__author__ = "730391057"

answer: str = "python"
word: str = input(f"What is your {len(answer)}-letter guess? ")
word_idx: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(word) != len(answer):
    word = input(f"That was not {len(answer)} letters! Try again: ")

if word != answer:
    print("Not quite. Play again soon! ")

    