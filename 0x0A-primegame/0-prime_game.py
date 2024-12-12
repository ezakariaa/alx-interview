#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def isWinner(x, nums):
    """
    Determine who wins the most rounds of the Prime Game.
    :param x: Number of rounds (integer).
    :param nums: List of n values, one for each round.
    :return: Name of the player with the most wins or None.
    """
    if not nums or x < 1:
        return None

    # Step 1: Generate primes up to the maximum value in nums using Sieve of Eratosthenes
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Step 2: Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:  # Odd number of primes -> Maria wins
            maria_wins += 1
        else:  # Even number of primes -> Ben wins
            ben_wins += 1

    # Step 4: Return the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

