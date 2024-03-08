"""Mutating functions."""

__author__ = "730602218"


def manual_append(word: list[int], a: int) -> None: 
    """Add to the end."""
    word.append(a)
    print(word)


def double(a: list[int]) -> None:
    """Double things in the list."""
    idx: int = 0
    while idx < len(a):
        a[idx] = a[idx] * 2
        idx += 1