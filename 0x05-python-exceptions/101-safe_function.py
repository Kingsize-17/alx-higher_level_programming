#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """The function that Executes a function safely.

    Args:
        fct: The function to be executed.
        args: Arguments for fct.

    Returns:
        Return - None If an error occurs.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
