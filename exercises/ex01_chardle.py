"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730391057"

word: str = input("Enter a 5-character word: ")

if len(str(word)) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(str(character)) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + str(character) + " in " + str(word))

if word[0] == character:
    print(str(character) + " found at index 0")

if word[1] == character:
    print(str(character) + " found at index 1")

if word[2] == character:
    print(str(character) + " found at index 2")

if word[3] == character:
    print(str(character) + " found at index 3")

if word[4] == character:
    print(str(character) + " found at index 4")

num_of_odds: int = 0

if word[0] == character:
    num_of_odds = num_of_odds + 1

if word[1] == character:
    num_of_odds = num_of_odds + 1

if word[2] == character:
    num_of_odds = num_of_odds + 1

if word[3] == character:
    num_of_odds = num_of_odds + 1

if word[4] == character:
    num_of_odds = num_of_odds + 1

if num_of_odds == 0:
    print("No instances of " + str(character) + " found in " + str(word))
else:
    if num_of_odds == 1:
        print(str(num_of_odds) + " instance of " + str(character) + " found in " + str(word))
    else:
        print(str(num_of_odds) + " instances of " + str(character) + " found in " + str(word))
