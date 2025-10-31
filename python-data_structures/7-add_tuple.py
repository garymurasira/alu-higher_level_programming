#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples and return a new tuple of 2 integers.
    If a tuple has less than 2 elements, missing values are treated as 0.
    Only the first 2 elements of each tuple are used.
    """
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a0 + b0, a1 + b1)
