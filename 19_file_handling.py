# File Handling in Python

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Welcome to Python file handling.")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Reading file content:")
    print(content)

# Appending to a file
with open("sample.txt", "a") as file:
    file.write("\nThis line is appended.")

# Reading file line by line
with open("sample.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())

# Writing a list of lines
lines = ["\nLine 1", "\nLine 2", "\nLine 3"]
with open("sample.txt", "a") as file:
    file.writelines(lines)

# Reading specific number of characters
with open("sample.txt", "r") as file:
    print("Reading first 10 characters:")
    print(file.read(10))

# File modes:
# 'r' - Read (default)
# 'w' - Write (overwrites file)
# 'a' - Append
# 'x' - Create new file, error if exists
# 'b' - Binary mode
# '+' - Read and write
