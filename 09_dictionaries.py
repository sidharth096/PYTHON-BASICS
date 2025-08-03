# Python Dictionaries – Key-Value Pairs

# Creating a dictionary
student = {
    "name": "Sidharth",
    "age": 25,
    "course": "Python"
}
print("Student info:", student)

# Accessing values
print("Name:", student["name"])
print("Course:", student.get("course"))  # safer access

# Changing values
student["age"] = 26
print("Updated age:", student["age"])

# Adding a new key-value pair
student["email"] = "sid@example.com"
print("After adding email:", student)

# Removing a key
student.pop("course")
print("After pop('course'):", student)

# Looping through dictionary
for key, value in student.items():
    print(key, "→", value)

# Keys and values
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

# Dictionary length
print("Number of items:", len(student))

# Clear dictionary
student.clear()
print("After clear():", student)
