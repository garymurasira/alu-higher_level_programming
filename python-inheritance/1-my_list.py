#!/usr/bin/python3
"""Module that defines MyList class"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Print the list in sorted ascending order"""
        print(sorted(self))


# Example usage
if __name__ == "__main__":
    my_list = MyList()
    my_list.append(3)
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(5)

    print("Original list:")
    print(my_list)

    print("Sorted list:")
    my_list.print_sorted()

    print("Original list after sorted print:")
    print(my_list)
