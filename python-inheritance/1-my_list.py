#!/usr/bin/python3
"""
This module defines MyList, a subclass of list with a custom print method.
"""


class MyList(list):
    """A list subclass with additional
    functionality for printing sorted contents."""
    def print_sorted(self):
        print(sorted(self))
