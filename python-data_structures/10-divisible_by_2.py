#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Returns a new list of True or False depending on whether
    each element in my_list is a multiple of 2.
    """
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
