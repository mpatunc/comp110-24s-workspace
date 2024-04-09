"""Recursion."""

__author__ = "730602218"


def f(n: int, k: int) -> int:
    """Function."""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return f(n - 1, k) + k