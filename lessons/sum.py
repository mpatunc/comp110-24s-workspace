"""Summing the elements of a list using different loops."""

__author__ = "730602218"


def w_sum(sum: list[float]) -> float: 
    """While loops."""
    idx: float = 0.0
    x: int = 0
    while x < len(sum): 
        idx += sum[x]
        x += 1
    return idx


def f_sum(sum: list[float]) -> float: 
    """For loops."""
    x: float = 0.0
    for idx in sum: 
        x += idx
    return x


def f_range_sum(sum: list[float]) -> float: 
    """Range."""
    x: float = 0.0
    for idx in range(0, len(sum)):
        x = x + sum[idx]
    return x