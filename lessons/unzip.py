"""Splitting a dictionary into two lists."""

__author__ = "730602218"


def get_keys(test: dict[str, int]) -> list[str]: 
    """Gets keys from dictionary."""
    key_list: list[str] = []
    for key in test: 
        key_list.append(key)
    return key_list


def get_values(test: dict[str, int]) -> list[int]: 
    """Gets values from dictionary."""
    key_list: list[int] = []
    for key in test: 
        if test[key]: 
            key_list.append(test[key])
    return key_list
        
        