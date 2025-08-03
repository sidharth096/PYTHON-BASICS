# Basic try-except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Try-except with multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Try-except-else
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("That's not a number.")
else:
    print("You entered:", value)

# Try-except-finally
try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("This will always run.")

# Raise an exception manually
# age = 15
# if age < 18:
#     raise Exception("You must be at least 18 years old.")
