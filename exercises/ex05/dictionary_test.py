"""Ex05 - Dictionary Functions Test."""

__author__ = "730602218"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
import pytest
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


# invert unit tests

# use case 1:
def test_invert_format() -> None:
    """Format of Function is correct."""
    dict1: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    dict2: dict[str, str] = {'z': 'a', 'y': 'b', 'x': 'c'}
    assert invert(dict1) == dict2


# use case 2: 
def test_invert_error() -> None: 
    """Error message present when repeats."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


# edge case:
def test_invert_empty() -> None: 
    """Empty dictionary."""
    dict1: dict[str, str] = {'': ''}
    dict2: dict[str, str] = {'': ''}
    assert invert(dict1) == dict2


# favorite color unit tests

# use case 1: 
def test_favorite_color_typical() -> None: 
    """Correct format."""
    color: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    max: str = "blue"
    assert favorite_color(color) == max


# use case 2: 
def test_favorite_color_equal() -> None: 
    """Equal votes for two colors -> only one should be returned."""
    color: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "yellow", "Jake": "yellow"}
    max1: str = "blue" and "yellow"
    assert favorite_color(color) == max1


# edge case: 
def test_favorite_color_same() -> None: 
    """All votes are the same color."""
    color: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "blue", "Jake": "blue"}
    max: str = "blue"
    assert favorite_color(color) == max


# count unit tests 


# use case 1
def test_count_normal() -> None: 
    """Proper number returned."""
    test_list: list[str] = ['cat', 'dog', 'bird', 'bunny']
    res_dict: dict[str, int] = {'cat': 1, 'dog': 1, 'bird': 1, 'bunny': 1}
    assert count(test_list) == res_dict


# use case 2
def test_count_duplicate() -> None: 
    """Includes multiple of the same item."""
    test_list: list[str] = ['cat', 'dog', 'dog', 'cat', 'bunny']
    res_dict: dict[str, int] = {'cat': 2, 'dog': 2, 'bunny': 1}
    assert count(test_list) == res_dict


# edge case 
def test_count_numbers() -> None: 
    """Works with numbers and special characters."""
    test_list: list[str] = ['cat', '1', '*', 'cat', 'bunny']
    res_dict: dict[str, int] = {'cat': 2, '1': 1, '*': 1, 'bunny': 1}
    assert count(test_list) == res_dict


# alphabetizer unit tests


# use case 1 
def test_alphabetizer_format() -> None: 
    """Format is correct."""
    test_list: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    res_dict: dict[str, list[str]] = {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
    assert alphabetizer(test_list) == res_dict


# use case 2 
def test_alphabetizer_case() -> None: 
    """Function is not case sensitive."""
    test_list: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    res_dict: dict[str, list[str]] = {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}
    assert alphabetizer(test_list) == res_dict


# edge case 
def test_alphabetizer_empty() -> None: 
    """Empty List."""
    test_list: list[str] = []
    res_dict: dict[str, list[str]] = {}
    assert alphabetizer(test_list) == res_dict


# update_attendance unit tests


# use case 1 
def test_update_attendance_format() -> None: 
    """Format is correct."""
    attendance: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_day: str = "Tuesday"
    update_name: str = "Vrinda"
    update_attendance(attendance, update_day, update_name)
    assert attendance == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda"]}


# use case 2
def test_update_attendance_multiple() -> None: 
    """Double name on same day is not repeated."""
    attendance: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_day: str = "Tuesday"
    update_names: list[str] = ["Kaleb", "Kaleb"]
    update_names = "Kaleb"
    update_attendance(attendance, update_day, update_names)
    assert attendance == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Kaleb"]}


# edge case 
def test_update_attendance_empty() -> None: 
    """Empty update."""
    attendance: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    no_day: str = ""
    no_names: list[str] = []
    assert update_attendance(attendance, no_day, no_names) == attendance[no_day].append(no_names)