#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in an ascending order."""

for i in range(9):
    for j in range(i + 1, 10):
        if i * 10 + j < 89:
            print("{:d}{:d}".format(i, j), end=", ")
print("{:d}".format(89))
