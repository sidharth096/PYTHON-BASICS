# Lambda Functions in Python – One-liner Anonymous Functions

# 1. Basic lambda function
square = lambda x: x * x
print("Square of 5:", square(5))

# 2. Lambda with multiple arguments
add = lambda a, b: a + b
print("Sum of 10 and 20:", add(10, 20))

# 3. Using lambda inside another function
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print("Double of 5:", double(5))

triple = multiplier(3)
print("Triple of 5:", triple(5))

# 4. Lambda with map() – apply function to each item in list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print("Squares using map:", squared)

# 5. Lambda with filter() – filter items based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)

# 6. Lambda with sorted() – sort by custom logic
names = ["ram", "sita", "lakshman", "bharat"]
sorted_names = sorted(names, key=lambda x: len(x))
print("Names sorted by length:", sorted_names)
