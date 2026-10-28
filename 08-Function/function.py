# Functions
# A function is a reusable block of code. Define it with def, then call it by name.
# This example reads three whole numbers, calculates their average, and prints it.

def avg():
    # input() returns text, so int() converts each answer to a whole number.
    a = int(input("Enter your first Number : "))
    b = int(input("Enter your second Number : "))
    c = int(input("Enter your third Number : "))

    # Divide the sum by the number of values to find the arithmetic mean.
    average = (a + b + c) / 3
    print(average)

# Calling the function runs the indented statements in its body.
avg()

# This function has no parameters and prints its result rather than returning it.
# Recursion is when a function calls itself; this example does not use recursion.