"""Math functions for calculator."""


def add(numbers):
    """Return the sum of the two inputs."""

    return sum(numbers)


def subtract(numbers):
    """Return the second number subtracted from the first."""
    total = 0
    for n in numbers[1:]:
        total += n
    return(numbers[0] - total)


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    return num1 / num2


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
