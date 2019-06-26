"""
    This module provides a list of primes from a exclusive max 
    number and an is_prime check method
    Exports:
    primes(n), is_prime(num)
"""

import math

__prime_nums = [2, 3, 5]


def primes(n):
    """Return a list of prime numbers less than the input number
    Parameters
    ----------
    n : int
    Returns
    -------
    list
        a list of numbers that are prime
    """
    for num in range(6, n):
        div_found = is_prime(num)
        if not div_found:
            __prime_nums.append(num)
    return __prime_nums


def is_prime(num):
    """Return True or False based on if the input is prime
    Parameters
    ----------
    num : int
    Returns
    -------
    bool
    """
    div_found = False
    sqrt = int(math.ceil(math.sqrt(num)))
    for prime in __prime_nums:
        if prime > sqrt:
            break
        elif num % prime == 0:
            div_found = True
            break
    return div_found
