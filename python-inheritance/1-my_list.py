#!/usr/bin/python3


class MyList(list):
    """
    A subclass of list that adds a method to print the list sorted.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order without
        modifying the original list.
        """
        return print(sorted(list))
