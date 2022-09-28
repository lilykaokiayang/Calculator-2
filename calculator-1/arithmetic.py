"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    sum = num1 + num2

    return sum


def subtract(num1, num2):
    """Return the value of num1 minus num2."""
    value = num1 - num2
    
    return value

def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    product = num1 * num2

    return product


def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    value = float(num1/num2)

    return value

def square(num1):
    """Return the square of num1."""
    squared = num1 ** 2
    
    return squared

def cube(num1):
    """Return the cube of num1."""
    cubed = num1 ** 3

    return cubed


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    power = num1 ** num2

    return power

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    remainder = num1 % num2

    return remainder
