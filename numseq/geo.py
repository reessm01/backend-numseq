"""
    This module provides basic geometric formulas.
    Exported functions:
    square(n), triangle(n), cube(n)
"""


def square(n):
    """Return the square of a number
    Parameters
    ----------
    n : int
    Returns
    -------
    int
    """
    return n * n


def triangle(n):
    """Return the triangle sum from a base number
    Parameters
    ----------
    n : int
    Returns
    -------
    int
    """
    return sum(range(n+1))


def cube(n):
    """Return the cube of a number
    Parameters
    ----------
    n : int
    Returns
    -------
    int
    """
    return n * n * n
