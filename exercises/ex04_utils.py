"""EX04 - List Utility Functions."""

__author__ = "730602218"


# all function: done
def all(list: list[int], a: int) -> bool:
    """All Function."""
    # if function has nothing in it
    if len(list) == 0: 
        return False
    else:
        idx: int = 0 
        while idx < len(list): 
            if list[idx] == a:
                # move through list to make sure all numbers equal 
                # while list[idx] == a: 
                idx += 1
            else:
                return False
        return True


# max function: done
def max(max_list: list[int]) -> int: 
    """Function to show max number in list."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    x: int = 0  
    max_num: int = max_list[0]
    while x < len(max_list): 
        if max_list[x] >= max_num: 
            max_num = max_list[x]
        x += 1
    return max_num


# is_equal function: done
def is_equal(a: list[int], b: list[int]) -> bool: 
    """Function to check if lists are equal."""
    # if lists are not the same size
    if len(a) != len(b): 
        return False
    # if the lists are the same size, then create idx that goes through each 
    # number to to see if the match. 
    else: 
        idx: int = 0
        while idx < len(a) and idx < len(b): 
            if a[idx] == b[idx]: 
                idx += 1
            else: 
                return False 
        return True


# extend function: in progress
def extend(a: list[int], b: list[int]) -> None:
    """Function to add two lists."""
    # for idx x in list b, add that to the end of the list. 
    for x in b: 
        # does not return anything 
        a.append(x)