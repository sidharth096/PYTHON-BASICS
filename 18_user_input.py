# USER INPUT IN PYTHON

# ============================
# 1. Basic input from user
# ============================

name = input("Enter your name: ")
print("Hello", name)

# ============================
# 2. Input with type conversion
# ============================

# All input is taken as string by default
age = input("Enter your age: ")
print("You are", age, "years old")

# Convert string to integer
age = int(age)
print("After 5 years, you will be", age + 5)

# ============================
# 3. Take multiple inputs in one line
# ============================

x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)

# ============================
# 4. Use map to convert multiple inputs at once
# ============================

a, b, c = map(int, input("Enter three numbers: ").split())
print("Product:", a * b * c)

# ============================
# 5. Float input example
# ============================

price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity: "))
total = price * quantity
print("Total cost:", total)
