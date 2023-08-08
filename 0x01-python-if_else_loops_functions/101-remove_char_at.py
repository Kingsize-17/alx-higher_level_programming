#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, n):
    """A copy of the string is created without the character at position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
