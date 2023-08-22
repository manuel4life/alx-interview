#!/usr/bin/python3

"""
A method that calculates the fewest number
of operations needed to result in exactly
"""


def minOperations(n):
    """
      A method that calculates the fewest number
      of operations needed to result in exactly
      n H characters in the file
    """
    if n <= 1:
        return 0

    operations = 0
    div = 2

    while n > 1:
        while n % div == 0:
            operations += div
            n /= div
        div += 1

    return operations
