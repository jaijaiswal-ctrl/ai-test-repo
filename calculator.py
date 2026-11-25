def add(a, b):
    result = a + b
    # Handle floating point precision issues
    if isinstance(result, float):
        return round(result, 10)
    return result


def subtract(a, b):
    result = a - b
    # Handle floating point precision issues
    if isinstance(result, float):
        return round(result, 10)
    return result


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    # Handle floating point precision issues
    if isinstance(result, float):
        return round(result, 10)
    return result