#!/usr/bin/python3
"""Module for the Prime Game."""


def isWinner(x, nums):
    """Determines the winner of multiple prime number removal games.

    Args:
        x (int): Number of games to be played.
        nums (list of int): List of upper limits for each game.

    Returns:
        str: The name of the winner, either "Ben" or "Maria".
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    m_ben = 0
    m_maria = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        remove_all_multiples(a, i)
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            m_ben += 1
        else:
            m_maria += 1
    if m_ben > m_maria:
        return "Ben"
    if m_maria > m_ben:
        return "Maria"
    return None


def remove_all_multiples(listers, x):
    """Marks multiples of a prime number as non-prime in a list.

    Args:
        ls (list of int): List where multiples will be marked.
        x (int): The prime number whose multiples are to be marked.
    """
    for index in range(2, len(listers)):
        try:
            listers[index * x] = 0
        except (ValueError, IndexError):
            break
