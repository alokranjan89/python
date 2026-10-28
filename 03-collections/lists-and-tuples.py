# Python Lists and Tuples - Important Notes
# Lists and tuples are used to store multiple values in one variable.
# They are ordered collections and support indexing.

# 1. List creation
numbers = [10, 20, 30, 40]
fruits = ["apple", "banana", "mango"]
mixed = [1, "hello", True, 3.5]
print(numbers)
print(fruits)
print(mixed)

# 2. List operations
# Access by index
print(numbers[0])      # 10
print(numbers[-1])     # 40
print(fruits[1])       # banana

# Slicing
print(numbers[1:3])    # [20, 30]
print(numbers[:3])     # [10, 20, 30]
print(numbers[::2])     # [10, 30]

# 3. List methods
# What each method does:
# append(value) -> adds a value at the end of the list
# insert(index, value) -> inserts value at a specific index
# remove(value) -> removes the first matching value
# pop() -> removes and returns the last element
# sort() -> sorts the list in ascending order
# reverse() -> reverses the order of the list
# len(list) -> returns number of elements
# count(value) -> counts how many times a value appears
# index(value) -> returns the index of the first matching value

numbers.append(50)     # add at end
print(numbers)          # [10, 20, 30, 40, 50]

numbers.insert(1, 15)  # insert at index 1
print(numbers)          # [10, 15, 20, 30, 40, 50]

numbers.remove(15)      # remove value 15
print(numbers)

numbers.pop()           # removes last element
print(numbers)

numbers.sort()          # sorts ascending
print(numbers)

numbers.reverse()       # reverse the list
print(numbers)

print(len(numbers))     # length of list
print(numbers.count(20))  # how many times 20 appears
print(numbers.index(30))  # index of value 30

# 4. List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)    # [1, 2, 3, 4, 5, 6]

# 5. List comprehensions
squares = [x * x for x in range(1, 6)]
print(squares)          # [1, 4, 9, 16, 25]

# 6. Tuple creation
coords = (10, 20)
colors = ("red", "green", "blue")
print(coords)
print(colors)

# 7. Tuple operations
# Tuple methods are limited because tuples are immutable.
# count(value) -> returns how many times a value appears
# index(value) -> returns the index of the first matching value
print(coords[0])        # 10
print(colors[1])        # green
print(colors[1:3])      # ('green', 'blue')
print(len(colors))      # 3
print(colors.count("green"))  # 1
print(colors.index("blue"))   # 2

# 8. Difference between list and tuple
# List is mutable (can change after creation)
# Tuple is immutable (cannot change after creation)

numbers[0] = 100
print(numbers)          # list can be modified

# tuple cannot be modified
# colors[0] = "yellow"   # This will raise TypeError

# 9. Important notes
# - Lists use [] and tuples use ()
# - Lists are mutable; tuples are immutable
# - Both are ordered and support indexing
# - Tuples are faster and safer for fixed data

# 10. Example loop
for item in fruits:
    print(item)
