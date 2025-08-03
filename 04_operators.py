# Python Operators Tutorial

# ------------------------------
# 1. Arithmetic Operators
# ------------------------------
# + (Addition), - (Subtraction), * (Multiplication), / (Division)
# % (Modulus), // (Floor Division), ** (Exponent)

a = 10
b = 20

print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)     # Remainder
print("a // b =", a // b)   # Floor division
print("a ** b =", a ** b)   # Exponentiation

print("\n=========================")

# ------------------------------
# 2. Assignment Operators
# ------------------------------
# =, +=, -=, *=, /=, %=, //=, **=

a = 10
print("Assignment Operators:")
a += 10   # a = a + 10 → 20
print("a += 10:", a)
a -= 5    # a = a - 5 → 15
print("a -= 5:", a)
a *= 2    # a = a * 2 → 30
print("a *= 2:", a)
a /= 3    # a = a / 3 → 10.0
print("a /= 3:", a)
a %= 4    # a = a % 4 → 2.0
print("a %= 4:", a)
a //= 2   # a = a // 2 → 1.0
print("a //= 2:", a)
a **= 3   # a = a ** 3 → 1.0
print("a **= 3:", a)

print("\n=========================")

# ------------------------------
# 3. Comparison Operators
# ------------------------------
# ==, !=, >, <, >=, <=

a = 10
b = 20

print("Comparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n=========================")

# ------------------------------
# 4. Logical Operators
# ------------------------------
# and, or, not

a = 10
b = 20

print("Logical Operators:")
print("a == 10 and b == 10:", a == 10 and b == 10)
print("a == 10 or b == 10:", a == 10 or b == 10)
print("not (a == 10):", not (a == 10))

print("\n=========================")

# ------------------------------
# 5. Identity Operators
# ------------------------------
# is, is not

a = 10
b = 10

print("Identity Operators:")
print("a is b:", a is b)         # True (in CPython, small ints are cached)
print("a is not b:", a is not b) # False

print("\n=========================")

# ------------------------------
# 6. Membership Operators
# ------------------------------
# in, not in

text = "python programming"

print("Membership Operators:")
print("'python' in text:", "python" in text)
print("'java' not in text:", "java" not in text)
