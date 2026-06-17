def divide(a, b):
    """Returns the result of dividing a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b