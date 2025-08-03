# Python Tuples – Immutable Ordered Collection

# Creating a tuple
fruits = ("apple", "banana", "cherry")
print("Original tuple:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("Sliced tuple (0:2):", fruits[0:2])

# Tuple length
print("Length of tuple:", len(fruits))

# Looping through tuple
for fruit in fruits:
    print("Fruit:", fruit)

# Tuples are immutable → this will raise an error:
# fruits[0] = "orange"  # ❌

# Tuple with one element (don't forget the comma)
single = ("only_one",)
print("Single-element tuple:", single)
