#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value in a dictionary.
    If the dictionary is empty or None, returns None.
    """
    if not a_dictionary:
        return None
    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key
