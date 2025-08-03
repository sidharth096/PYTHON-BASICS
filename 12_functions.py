# Python Functions – Reusable Blocks of Code

# 1. Defining and calling a basic function
def greet():
    print("Hello, welcome to Python!")

greet()  # Calling the function

print("\n=========================\n")

# 2. Function with parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Sidharth")

print("\n=========================\n")

# 3. Function with return value
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

print("\n=========================\n")

# 4. Function with default arguments
def multiply(a, b=2):
    return a * b

print("Multiply with default:", multiply(5))      # b uses default
print("Multiply with both:", multiply(5, 3))      # both values passed

print("\n=========================\n")

# 5. Function with keyword arguments
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person(age=25, name="Ram")  # order doesn't matter

print("\n=========================\n")

# 6. Function with variable number of arguments
def print_numbers(*nums):
    for number in nums:
        print("Number:", number)

print_numbers(1, 2, 3, 4)

print("\n=========================\n")

# 7. Nested function
def outer():
    def inner():
        print("Inside inner function")
    print("Inside outer function")
    inner()

outer()
