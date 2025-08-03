# Mathematical Operations in Python

import math # Import the inbuilt math module

# 1. Absolute value
num = -10
print("Absolute:", abs(num))  # 10

# 2. Power
print("2^3:", pow(2, 3))  # 8

# 3. Square root
print("Square root of 16:", math.sqrt(16))  # 4.0

# 4. Ceiling and Floor
num = 4.6
print("Ceiling:", math.ceil(num))  # 5
print("Floor:", math.floor(num))   # 4

# 5. Trigonometry
print("Sine of 90 degrees:", math.sin(math.radians(90)))  # 1.0
print("Cosine of 0 degrees:", math.cos(math.radians(0)))  # 1.0

# 6. Constants
print("PI:", math.pi)
print("Euler's Number (e):", math.e)

# 7. Logarithm
print("Log base e of 10:", math.log(10))       # Natural log
print("Log base 10 of 100:", math.log10(100))  # Base 10 log

# 8. Factorial
print("Factorial of 5:", math.factorial(5))  # 120

# 9. Modulo operation
print("10 % 3 =", 10 % 3)

# 10. Round a number
print("Round 4.567 to 2 decimal places:", round(4.567, 2))
