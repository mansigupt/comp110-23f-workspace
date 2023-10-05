"""Quiz01 practice"""

my_number_string: str = input("Guess a number: ")
my_number: int = int(my_number_string)

if my_number % 3 != 0:
    print("A")
elif my_number > 4:
    print("B")
else:
    print("C")

if my_number + 1 <= 18:
    print("D")