"""Mutable vs Immutable."""


# mutable: can be mutated (changed) after creation 
# Mutable types: lits and dicts
# can be both reassigned and changed 
# can be mutated directly, but also with functions


# immutable: can't be mutated (changed) after creation 
# immutable types: int, float, str, bool, and tuple
# can be reassigned, but not changed 


# remove first element 
def remove_first(input_list: list[str]) -> None: 
    """Remove first. -> Mutating!"""
    input_list.pop(0)


# get first elem
def get_first(input_list: list[str]) -> str:
    """Return first elem of list without mutating."""
    return input_list[0]


# get and remove first elem 
def get_and_remove_first(input_list: list[str]) -> str: 
    """Return first element AND remove it."""
    elem: str = input_list[0]
    input_list.pop(0)
    return elem
