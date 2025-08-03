# Python Sets – Unordered Collection with Unique Items

# Creating a set
colors = {"red", "green", "blue", "red"}  # duplicates are removed
print("Original set:", colors)

# Add an element
colors.add("yellow")
print("After add('yellow'):", colors)

# Update with multiple elements
colors.update(["pink", "black"])
print("After update():", colors)

# Remove an element (will error if not found)
colors.remove("red")  # use discard() if unsure
print("After remove('red'):", colors)

# Discard element (no error if not found)
colors.discard("orange")  # safe remove
print("After discard('orange'):", colors)

# Pop a random item
colors.pop()
print("After pop():", colors)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print("Union:", set1 | set2) # same as set1.union(set2)
print("Union:", set3) # same as set1 | set2
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Clear the set
colors.clear()
print("After clear():", colors)



