# ASSIGNMENT 7: STRINGS AND TUPLES

# 1. STRING CONCATENATION

print("1. STRING CONCATENATION")

str1 = "Hello"
str2 = input("Enter your name: ")

# Concatenate two strings
result = str1 + " " + str2
print("Concatenated string:", result)

# Add the third string
result = result + ", welcome to Python programming"
print("Final string:", result)


# 2. STRING SLICING AND INDEXING

print("\n2. STRING SLICING AND INDEXING")

# First character
print("First character:", result[0])

# Last character
print("Last character:", result[-1])

# First 5 characters
print("First 5 characters:", result[:5])

# Last 11 characters
print("Last 11 characters:", result[-11:])

# Reverse the string
print("Reversed string:", result[::-1])

# Extract the word Python
print("Word Python:", result[result.index("Python"):result.index("Python") + 6])


# 3. STRING METHODS

print("\n3. STRING METHODS")

strM = "Python beginner tutorial"

# Convert to uppercase
print("Uppercase:", strM.upper())

# Convert to lowercase
print("Lowercase:", strM.lower())

# Capitalize the sentence
print("Capitalized:", strM.capitalize())

# Count occurrences of 't'
print("Count of 't':", strM.count("t"))

# Replace Python with Machine Learning
print("Replaced string:", strM.replace("Python", "Machine Learning"))


# 4. TUPLES

print("\n4. TUPLES")

# Create two tuples
t1 = (10, 20)
t2 = (40, 50, 60)

# Concatenate tuples
t_combine = t1 + t2
print("Combined tuple:", t_combine)

# Repeat the tuple 3 times
print("Repeated tuple:", t_combine * 3)

# Access the third element
print("Third element:", t_combine[2])

# Access the first three elements
print("First three elements:", t_combine[:3])

# Access the last three elements
print("Last three elements:", t_combine[-3:])