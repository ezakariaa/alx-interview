#!/usr/bin/python3
"""Change making module."""


def makeChange(coins, total):
    """Determines the fewest number of coins needed."""
    if total <= 0:
        return 0
    remember = total
    counter = 0
    index = 0
    mycoins = sorted(coins, reverse=True)
    limit = len(coins)
    while remember > 0:
        if index >= limit:
            return -1
        if remember - mycoins[index] >= 0:
            remember -= mycoins[index]
            counter += 1
        else:
            index += 1
    return counter
