# Functions and Recursion

Run the examples from the repository root:

```bash
python 08-Function/function.py
python 08-Function/recursion.py
```

`function.py` demonstrates a function that reads three numbers and prints
their average. `recursion.py` demonstrates countdown, factorial, and summing
numbers with recursive functions.

## What is recursion?

Recursion is a technique where a function solves a problem by calling itself
with a smaller or simpler version of that problem. Each call works on its own
arguments and local variables.

A correct recursive solution needs all of the following:

1. **Base case:** a condition for the smallest case, solved without another
   recursive call.
2. **Recursive case:** the function calls itself to handle a smaller case.
3. **Progress:** every recursive call moves closer to a base case.
4. **A result path:** for functions that return values, each call combines or
   passes along the result it receives.

Without a reachable base case, or if calls do not make progress toward it, the
function keeps calling itself until Python raises `RecursionError`.

## Countdown example

```python
def countdown(number):
    if number <= 0:       # base case
        print("Done!")
        return

    print(number)
    countdown(number - 1) # recursive case: number gets smaller
```

Calling `countdown(3)` prints `3`, `2`, `1`, then `Done!`. The `return` in the
base case stops that call from continuing.

## Returning a result: factorial

The factorial of a non-negative integer is the product of all positive
integers up to it. By definition, `0!` is `1`.

```python
def factorial(number):
    if number < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if number == 0:                 # base case
        return 1
    return number * factorial(number - 1)
```

For `factorial(4)`, the calls build this chain:

```text
factorial(4) -> 4 * factorial(3)
             -> 4 * 3 * factorial(2)
             -> 4 * 3 * 2 * factorial(1)
             -> 4 * 3 * 2 * 1 * factorial(0)
             -> 4 * 3 * 2 * 1 * 1 = 24
```

The calls first go deeper until the base case. Then they return in reverse
order, each completing its multiplication. This is often called **unwinding**
the call stack.

## The call stack and limits

Python keeps track of active function calls on a **call stack**. Each recursive
call uses another stack frame containing its arguments and local state. A deep
recursion can use substantial memory; Python also enforces a recursion limit.
Do not raise that limit as a routine fix—use a loop or a different algorithm
when the input may require very deep recursion.

## Recursion compared with loops

- Recursion can make naturally nested problems easier to express, such as
  walking a tree or breaking a problem into similar subproblems.
- A loop is usually simpler and more memory-efficient for straightforward
  repetition, such as counting from 1 to a large number.
- In Python, recursive calls do not get tail-call optimization, so even a
  recursive function whose final action is another call still uses stack
  frames.
- Some recursive algorithms repeat work. A simple recursive Fibonacci
  implementation is a common example; use memoization or an iterative
  algorithm if performance matters.

## Common mistakes

- **No base case:** every call keeps recursing.
- **Unreachable base case:** the input moves away from, rather than toward,
  the stopping condition.
- **Forgetting to return:** a caller receives `None` instead of the computed
  result.
- **Wrong base-case result:** for example, factorial's base case must return
  `1`, because it is the identity for multiplication.
- **No input validation:** define how invalid inputs such as negative
  factorial arguments should behave.
- **Testing only one input:** test the base case, a small normal case, and
  invalid or boundary inputs.

## Practice

1. Write `sum_to(n)` recursively so `sum_to(4)` returns `10`.
2. Write a function that returns the number of digits in a positive integer.
3. Write a function that reverses a string recursively.
4. For each function, identify its base case and explain why each call gets
   closer to it. Then consider whether a loop would be clearer.

The first exercise is implemented as `sum_to` in `recursion.py`.
