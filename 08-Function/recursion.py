"""Small examples of recursive functions."""


def countdown(number: int) -> None:
    """Print numbers down to 1, then stop at the base case."""
    if number <= 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)


def factorial(number: int) -> int:
    """Return n! for a non-negative integer n."""
    if number < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if number == 0:
        return 1

    return number * factorial(number - 1)


def sum_to(number: int) -> int:
    """Return the sum of all integers from 1 through number."""
    if number < 0:
        raise ValueError("number must be non-negative")
    if number == 0:
        return 0

    return number + sum_to(number - 1)


if __name__ == "__main__":
    print("Countdown:")
    countdown(3)

    print("\nFactorial:")
    print(f"5! = {factorial(5)}")

    print("\nSum from 1 through 5:")
    print(sum_to(5))
