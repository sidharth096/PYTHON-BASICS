# Python List – Collection Data Type

# Creating a list
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Length of the list
print("Length of list:", len(numbers))

print("\n=========================\n")

# Adding elements

# Append: add element at the end
numbers.append(6)
print("After append(6):", numbers)

# Insert: add element at a specific index
numbers.insert(1, 7)  # Insert 7 at index 1
print("After insert(1, 7):", numbers)

print("\n=========================\n")

# Removing elements

# Remove by value
numbers.remove(7)
print("After remove(7):", numbers)

# Pop: removes the last element
numbers.pop()
print("After pop():", numbers)

# Pop with index: removes specific index
numbers.pop(1)
print("After pop(1):", numbers)

print("\n=========================\n")

# Slicing the list
print("Sliced list (1:4):", numbers[1:4])

# Clearing all elements
numbers.clear()
print("After clear():", numbers)

print("\n=========================\n")

# Deleting the entire list (commented for safety)
# del numbers
# print(numbers)  # This will throw an error because the list is deleted
