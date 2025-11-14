#!/usr/bin/python3
"""Module that defines MyList class"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Print the list in sorted ascending order"""
        print(sorted(self))
