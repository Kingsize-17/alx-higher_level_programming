#!/usr/bin/python3


def print_safe_integer(value):
    """This is printing an integer with "{:d}".format().

    Args:
        value(in): The integers to be printed.

    Returns:
        Return - False if a TypeError or ValueError occurs.
        Otherwise print - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
