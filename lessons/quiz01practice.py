"""Quiz01 practice"""


x: str = int(input("Pick a number: "))
y: int = 10
z: int = 2
x = x - 1
if x < 10:
    print("A")
elif (x % z) == 0:
    print("B")
if x == (y + z):
    print("C")
else:
    print("D")
