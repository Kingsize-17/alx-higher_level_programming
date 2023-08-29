#!/usr/bin/python3

import sys


def print_safe_integer_err(value):
    """Prints an integer withb the "{:d}".format().

    If a ValueError message is encountered, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to be printed.

    Returns:
        False - If a TypeError or ValueError occurs.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
