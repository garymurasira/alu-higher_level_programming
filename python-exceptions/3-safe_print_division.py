#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result.
    Uses try/except/finally. Returns result or None.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
