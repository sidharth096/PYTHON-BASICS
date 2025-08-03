# Python Conditional Statements

# 1. Simple if condition
age = 18

if age >= 18:
    print("You are eligible to vote.")

print("\n=========================\n")

# 2. if-else condition
temperature = 35

if temperature > 30:
    print("It's a hot day.")
else:
    print("It's a cool day.")

print("\n=========================\n")

# 3. if-elif-else condition
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D or Fail")

print("\n=========================\n")

# 4. Nested if condition
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful!")
    else:
        print("Wrong password.")
else:
    print("Username not found.")

print("\n=========================\n")

# 5. One-line if statement
x = 5
y = 10
print("x is greater") if x > y else print("y is greater")

print("\n=========================\n")

# 6. Using logical operators with conditions
logged_in = True
is_admin = False

if logged_in and is_admin:
    print("Access to admin panel")
elif logged_in:
    print("Logged in as user")
else:
    print("Please log in first")
