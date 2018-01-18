#!/usr/bin/python3
"""
Module content
14-pascal_triangle   - Return a list of lists of integers representing
                       Pascal's triangle of n
"""


def pascal_triangle(n):
    """ Return a list of lists of integers representing triangle of n """
    answer = []
    row = []

    if (n <= 0):
        return (answer)

    for i in range(1, n+1):
        # Going from right to left. Adding 1 to end of row list
        row.append(1)

        for j in range(i-2, 0, -1):
            # Updating row value from right to left
            row[j] += row[j-1]

        answer.append(row * 1)

    return (answer)
