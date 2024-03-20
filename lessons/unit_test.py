"""Test sum functionality"""

from lessons.unit import sum

# syntax 
    # def test_name() -> None: 
        # assert <boolean expressions> 
# command line: python -m pytest path/to/testfile.py
# test file names: ends with _test.py
# test functions names: begin with test_ 

# use case: testing properties for how we expect our programs to be used 
# edge case: test instances outside "typical" usage

# function to test the "sum" function
def test_sum_empty() -> None: 
    assert sum([]) == 0 

# to actually test go into 
# terminal and type python -m pytest [where your function is
# for example python -m pytest lessons/unit_test.py for this function
    
def test_sum_one_elements() -> None:
    """Sum of one element should return that element."""
    test: list[int] = [7]
    assert sum(test) == 7 
    

def test_sum_positive() -> None:
    """Sum of positive numbers should return sum of those numbers."""
    test: list[int] = [2, 4, 6]
    assert sum(test) == 12 


def test_sum_with_negative() -> None: 
    """Sum should work with positive and negative numbers."""
    test: list[int] = [2, -2, 4]
    assert sum(test) == 4