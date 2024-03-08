"""Ex05 - Dictionary Functions(Invert Function)."""

__author__ = "730602218"


# done
# invert function makes keys values, and values keys.
def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert Keys and Values."""
    for key in input: 
        # new variable to look at vales in input
        # allows us to compare strs 
        repeat: str = input[key]
        # for loop to look through each sting and see if there is repetition 
        for x in input: 
            if key != x and repeat == input[x]:
                raise KeyError("cannot have the same keys.")
    
    # new list for hold reversed list.
    rev_dict: dict[str, str] = {}
    # create a for loop for iterate through list
    for key in input: 
        rev_dict[input[key]] = key
    return rev_dict
    

# done
# favorite color function finds most popular color in list
def favorite_color(colors: dict[str, str]) -> str: 
    """Find Favorite Color in Dictionary."""
    pop_col: dict[str, int] = {}
    for name in colors: 
        if colors[name] in pop_col: 
            pop_col[colors[name]] += 1
        else: 
            pop_col[colors[name]] = 1 
    max: str = ""
    idx: int = 0 
    for num in pop_col: 
        x: int = pop_col[num]
        if x >= idx: 
            idx = x
            max = num 
    return max


# done 
def count(input: list[str]) -> dict[str, int]:
    """Shows how many times a value shows up in the list."""
    # new list 
    res_dict: dict[str, int] = {}
    for key in input: 
        if key in res_dict: 
            res_dict[key] += 1
        else: 
            res_dict[key] = 1 
    return res_dict


# not adding multiple of the same letters in the list 
# alphabetical order function 
def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Sorts list depending on first letter."""
    res_dict: dict[str, list[str]] = {}
    for word in input: 
        # for key in input: 
        # first letter in x 
        # add .lower() here to make sure it is not case sensitive? 
        first_l = word[0].lower()
        # if first_l is not in list, then make it into a key
        if first_l not in res_dict:
            # and first_l == word[0]: 
            res_dict[first_l] = [word]
        # if it is in the list, then append the key into the value part of the dictionary
        else: 
            res_dict[first_l].append(word)
    # return result dictionary
    return res_dict


# attendance function 
def update_attendance(imp_list: dict[str, list[str]], day: str, name: str) -> None:
    """Updates attendance.""" 
    # if day is in the attendance list...
    if day in imp_list: 
        # then append that name to that day in the list.  
        imp_list[day].append(name)
    else: 
        # if not, then add a new name to the list.
        imp_list[day] = [name]