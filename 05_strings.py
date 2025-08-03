# Python Strings – Basic Operations and Formatting

# String declaration
greeting = "hello everyone"
raw_message = "    hi "

# Accessing characters and slicing
print("Original greeting:", greeting)
print("First character:", greeting[0])
print("Last character:", greeting[-1])
print("Sliced (0:4):", greeting[0:4])           # 'hell'
print("Sliced with step (0:9:2):", greeting[0:9:2])  # every 2nd character
print("Reversed string:", greeting[::-1])

print("\n=========================\n")

# String methods
print("Raw message with spaces:", repr(raw_message))  # shows spaces
print("After strip():", raw_message.strip())          # removes spaces
print("Uppercase:", raw_message.upper())
print("Lowercase:", raw_message.lower())
print("Replace 'h' with 'H':", raw_message.replace("h", "H"))

print("\n=========================\n")

# String concatenation
combined_message = raw_message + greeting
print("Combined message:", repr(combined_message))

print("\n=========================\n")

# String formatting using format()
user_name = "Ram"
sentence_one = "My name is {}. I am 50 years old."
sentence_two = "My name is {}. I am {} years old."

print("Formatted sentence 1:", sentence_one.format(user_name))         # positional arguments
print("Formatted sentence 2:", sentence_two.format(user_name, 50)) # positional arguments
print ("formatted sentence :" f"My name is {user_name}. I am {50} years old.") # f-string

print("\n=========================\n")

# Optional: Using f-strings (modern and readable)
print(f"Using f-string: My name is {user_name}. I am {50} years old.")
