# Python Strings - Important Notes
# A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.

name = "Alok"
message = 'Hello, World!'
paragraph = """This is a multi-line
string example."""

# 1. String creation
# Strings can be created using single quotes or double quotes.
first_name = 'Alice'
last_name = "Kumar"
print(first_name, last_name)

# 2. String concatenation
full_name = first_name + " " + last_name
print(full_name)     # Alice Kumar

# 3. String repetition
print("Hi! " * 3)  # Hi! Hi! Hi!

# 4. Indexing and slicing
word = "Python"
print(word[0])      # P
print(word[-1])     # n
print(word[0:3])    # Pyt
print(word[:4])     # Pyth
print(word[2:])     # thon

# 4.1 Slicing with skip value (step)
# The third value in slicing is the step size.
# It tells Python how many characters to skip between each character.
print(word[::2])    # Pto
print(word[1::2])   # yhn
print(word[::-1])   # nohtyP
# The step can be positive or negative.
# - word[::2] -> take every 2nd character
# - word[::-1] -> reverse the string

# 5. String length
print(len(word))    # 6

# 6. String methods
text = "  hello world  "
print(text.strip())          # 'hello world'
print(text.upper())          # '  HELLO WORLD  '
print(text.lower())          # '  hello world  '
print(text.title())          # '  Hello World  '
print(text.replace("world", "Python"))
print(text.split())          # ['hello', 'world']

# 7. String membership
print("h" in "hello")       # True
print("x" in "hello")       # False

# 8. Escape characters
print("Hello\nWorld")       # New line
print("Hello\tWorld")       # Tab
print("He said \"Hi\"")   # Quotes inside string

# 9. Formatting strings
age = 25
print(f"My age is {age}")
print("My age is {}".format(age))

# 10. Common string functions
msg = "Learning Python is fun"
print(msg.count("a"))
print(msg.find("Python"))
print(msg.startswith("Learning"))
print(msg.endswith("fun"))

# 10.1 More important string functions
text = "Python Programming"
print(text.upper())          # PYTHON PROGRAMMING
print(text.lower())          # python programming
print(text.capitalize())     # Python programming
print(text.title())          # Python Programming
print(text.swapcase())      # pYTHON pROGRAMMING
print(text.strip())          # removes spaces from both ends
print(text.replace("Python", "Java"))  # Java Programming
print(text.split())          # ['Python', 'Programming']
print("-".join(["Python", "Java"]))  # Python-Java
print(text.isalpha())        # False (space present)
print("Python".isalpha())    # True
print("123".isdigit())      # True
print("   ".isspace())      # True
print(text.startswith("Py"))  # True
print(text.endswith("ing"))  # True

# 11. Important notes
# - Strings are immutable, which means they cannot be changed after creation.
# - String operations create new strings instead of modifying the original.
# - Indexing starts from 0.
# - Strings can be used in loops and condition checks.

# Example:
for ch in "Alok":
    print(ch)

