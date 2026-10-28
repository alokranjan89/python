# Python Dictionaries and Sets - Important Notes
# Dictionaries and sets are built-in data structures for storing multiple related values.
# A dictionary stores data as key-value pairs.
# A set stores unique values and is useful for membership checks and removing duplicates.

# 1. Dictionary creation
student = {
    "name": "Aisha",
    "age": 20,
    "course": "Python"
}
print(student)
print(student["name"])   # Aisha

# 2. Adding and updating values
student["grade"] = "A"
student["age"] = 21
print(student)

# 3. Accessing dictionary values
print(student.get("course"))     # Python
print(student.keys())             # all keys
print(student.values())           # all values
print(student.items())            # key-value pairs

# 4. Removing entries
student.pop("grade")
print(student)

# Using del to remove a specific key
# del student["course"]
# print(student)

# 5. Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# 6. Nested dictionaries
student_profile = {
    "name": "Sam",
    "details": {
        "city": "Lagos",
        "country": "Nigeria"
    }
}
print(student_profile["details"]["city"])  # Lagos

# 7. Set creation
numbers = {1, 2, 3, 3, 4, 5}
print(numbers)  # duplicates are removed automatically

# A set can also be created from a list
letters = set(["a", "b", "a", "c"])
print(letters)

# 8. Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a | set_b)   # union
print(set_a & set_b)   # intersection
print(set_a - set_b)   # difference
print(set_a ^ set_b)   # symmetric difference

# 9. Membership test
print(3 in set_a)      # True
print(10 in set_a)     # False

# 10. Important notes
# - Dictionaries use {} with key: value pairs
# - Keys in a dictionary must be unique
# - Dictionaries are mutable and allow updates
# - Sets use {} but only store unique values
# - Sets are unordered and do not support indexing
# - Sets are useful when you need fast membership checks or unique values

# 11. Properties and use of dictionaries
# Dictionary properties:
# - Stores data as key-value pairs
# - Fast lookups by key
# - Keys must be unique, values can repeat
# - Keeps related data together, such as user information or settings
# - Can be modified after creation
#
# Common dictionary uses:
# - Storing configuration values
# - Representing records or objects
# - Counting repeated words or values
# - Creating lookup tables for mapping IDs to data

# Example: counting letters in a word
word = "banana"
letter_count = {}

for ch in word:
    letter_count[ch] = letter_count.get(ch, 0) + 1

print(letter_count)

# 12. Properties and use of sets
# Set properties:
# - Contains only unique values
# - Unordered, so elements have no fixed index
# - Supports fast membership testing with "in"
# - Useful for mathematical set operations like union and intersection
#
# Common set uses:
# - Removing duplicates
# - Checking whether a value exists
# - Comparing different groups of data
# - Tracking visited items or completed tasks

# Example use case
# A set is often used to track seen items while processing data.
seen = set()
items = ["apple", "banana", "apple", "mango"]

for item in items:
    if item not in seen:
        seen.add(item)
        print(f"New item added: {item}")

print(seen)

# e = set() Empty Set