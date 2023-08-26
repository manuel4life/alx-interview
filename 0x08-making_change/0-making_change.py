#!/usr/bin/python3

"""
A function thatdetermine the fewest number
of coins neededto meet a given amount total.
Prototype: def makeChange(coins, total)Return:
fewest number of coins needed to meet total.
"""


def makeChange(coins, total):

    """
    A function thatdetermine the fewest number
    of coins neededto meet a given amount total.
    Prototype: def makeChange(coins, total)Return:
    fewest number of coins needed to meet total.
    If total is 0 or less, return 0 If total cannot
    be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            new_min = min_coins[amount - coin] + 1
            min_coins[amount] = min(min_coins[amount], new_min)

    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
