# Recursion in Python – Function calling itself

# 1. Simple Recursive Function: Print numbers from n to 1
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)

print("Printing numbers from 5 to 1:")
print_numbers(5)

print("=========================")

# 2. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

print("=========================")

# 3. Fibonacci Series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci series (first 6 terms):")
for i in range(6):
    print(fibonacci(i), end=" ")

print("\n=========================")

# 4. Sum of natural numbers using recursion
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

print("Sum of first 5 natural numbers:", sum_natural(5))
