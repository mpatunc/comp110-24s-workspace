"""For fun."""


def value_exists(test_dict: dict[str, int], test_val: int) -> bool: 
    """Function."""
    for key in test_dict:
        if test_val == test_dict[key]: 
            return True
    return False


def plus_or_minus_n(inp: dict[str, int], n: int) -> None: 
    """Function."""
    for key in inp:
        if inp[key] % 2 == 0: 
            inp[key] += n
        else: 
            inp[key] -= n