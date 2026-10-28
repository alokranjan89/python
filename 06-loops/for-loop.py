# Python loops - Important Notes
# A loop allows you to repeat a block of code multiple times.
# This is useful when you want to perform the same action on many values.

# 1. For loop
# A for loop is used when you know how many times you want to repeat.
# The range() function generates numbers from a start value up to but not including the end value.

for i in range(1, 6):
    print(i)

# 2. What this does
# range(1, 6) gives: 1, 2, 3, 4, 5
# The code inside the loop runs once for each number.

# 3. While loop
# A while loop keeps running as long as a condition is True.
count = 1
while count <= 5:
    print(count)
    count += 1

# 4. Important notes
# - Use for loops when the number of repetitions is known.
# - Use while loops when the number of repetitions depends on a condition.
# - Python uses indentation to show which statements belong to the loop.
# - Be careful with while loops to avoid infinite loops.

# 5. Common use cases
# - Printing a list of values
# - Repeating calculations
# - Iterating through items in a collection
# - Processing user input until a condition changes

# 6. Example: summing numbers
sum_value = 0
for num in range(1, 6):
    sum_value += num
print("Sum:", sum_value)

# 7. Example: breaking out of a loop
for num in range(1, 11):
    if num == 6:
        break
    print(num)
