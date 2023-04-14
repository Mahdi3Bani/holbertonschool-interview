#!/usr/bin/python3
"""In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n"""


def minOperations(n):
    """method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file"""
    if n <= 1:
        return 0

    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)

    return sum(factors)
