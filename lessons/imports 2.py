"""Practice importing from other modules."""

# from <package name>.<module name> import <function name>
from lessons.my_functions import addition

# <module name>.<function name>(arguments)
# print(my_functions.addition(1,2))

# <module name>.<variable name>
# print(my_functions.my_variable)

if __name__ == "__main__":
    print("Howdy!")

print(addition(1,2))