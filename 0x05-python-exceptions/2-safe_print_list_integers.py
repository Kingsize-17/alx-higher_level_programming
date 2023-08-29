#!/usr/bin/python3

def print_safe__list_integers(my_list = [], x=0):
    """This prints the first x elements of a list that are integers.

    Args:
        my_list(list): The list from where the elements are printed from.
        x (int): The number of elements of my_list to be printed.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
