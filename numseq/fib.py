"""
    This module provides a way to determine a Fibonacci 
    number from a given nth sequence.
    Exports:
    fib(n)
"""

def fib(n):
    """Return the Fibonacci's number from the nth sequence
    Parameters
    ----------
    n : int
    Returns
    -------
    int
    """
    seq = [0, 1]
    while len(seq) < n:
        seq += [seq[-1] + seq[-2]]
    return seq[-1] if n > 0 else seq[n]