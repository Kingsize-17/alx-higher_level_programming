#!/usr/bin/python3

def print_safe_list(my_list = [], x=0):
    """Print the x elememts of a list.

    Args:
        my_list: The list to print the elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        return the number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
