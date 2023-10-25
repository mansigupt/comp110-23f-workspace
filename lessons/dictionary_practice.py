# Setting up a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary.")

# Adding a key & value in dictionary
ice_cream["mint"] = 3
print("After adding mint: ")
print(ice_cream)

# Removing a key in a dictionary
ice_cream.pop("mint")
print("After removing mint: ")
print(ice_cream)

# Adjusting the value of a specific key in a dictionary
print(f"There are {ice_cream['chocolate']} orders of chocolate")
ice_cream["vanilla"] = 10
# ice_cream += 2
print("After adjusting the amount of vanilla: ")
print(ice_cream)

# The length is the number of key value pairs
print(f"The length of my dictionary is {len(ice_cream)}")

# Checking if value is in dictionary
print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)

print("Is mint in ice_cream?")
print("mint" in ice_cream)

# Using it in a conditional
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint!")
else:
    print("No orders of mint!")

if "chocolate" in ice_cream:
    print(f"There are {ice_cream['chocolate']} orders of chocolate!")
else:
    print("No orders of chocolate!")

# Loop through and print out every flavor and its number of orders
for key in ice_cream:
    # print <flavor> has <num_orders> orders
    print(f"{key} has {ice_cream[key]} orders")