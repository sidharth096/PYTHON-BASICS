# Python Loops – for and while

# 1. for loop with a list
fruits = ["apple", "banana", "cherry"]

print("For loop over list:")
for fruit in fruits:
    print("Fruit:", fruit)

print("\n=========================\n")

# 2. for loop with range()
print("For loop with range:")
for i in range(1, 6):
    print("Number:", i)

print("\n=========================\n")

# 3. while loop
count = 1

print("While loop:")
while count <= 5:
    print("Count is:", count)
    count += 1

print("\n=========================\n")

# 4. break statement
print("Break statement in loop:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\n=========================\n")

# 5. continue statement
print("Continue statement in loop:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n=========================\n")

# 6. else with loops
print("Else with for loop:")
for i in range(3):
    print(i)
else:
    print("Loop finished without break.")

print("\n=========================\n")

print("Else with while loop:")
x = 1
while x < 4:
    print(x)
    x += 1
else:
    print("While loop completed.")
