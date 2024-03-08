"""Some functions for my garden plan!"""

__author__ = "730602218"


# by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
# print(by_kind)


# new_plant: str = "elderberry"
# new_plants_kind: str = "fruit"


# Function name: add_by_kind
# Parameters: dict[str, list[str]], str, str
# Return Type: None
# want to get: {"flower": ["marigold", "zinnia", (add daisy) "daisy"], "vegetable": ["carrots"]}


def add_by_kind(by_kind: dict[str, list[str]], new_plants_kind: str, new_plant: str) -> None: 
    """Add plant under its kind."""
    # if kind is already in dict (flower already in dict)
    if new_plants_kind in by_kind:
        by_kind[new_plants_kind].append(new_plant)
    else:  # if kind not in dict (fruit not in dict)
        by_kind[new_plants_kind] = [] 
        by_kind[new_plants_kind].append(new_plant)


def add_by_date(garden_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under date to sow seeds."""
    if month in garden_by_date: 
        garden_by_date[month].append(plant)
    else: 
        garden_by_date[month] = []
        garden_by_date[month].append(plant)


# Function name: lookup_by_kind_and_date
# Parameters: dict[str, list[str]], dict[str, list[str]], str, str
# Return Type: str


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str: 
    """Return str with list of plants of a specific kind to plant in a specific month."""
    assert kind in plants_by_kind
    assert month in plants_by_date
    # get a list of all plants of a specific kind 
    kind_list: list[str] = plants_by_kind[kind] 
    # get a list if all plants in same month 
    month_list: list[str] = plants_by_date[month]
    # go through both lists and find elements that appear in both
    # kind_list = ["marigold", "daisy"]
    # month_list = ["daisy", "rose"]
    combined_list: list[str] = []
    for plant in kind_list: 
        for other_plant in month_list: 
            if plant == other_plant:  # plant if both in kind_list and month_list
                combined_list.append(other_plant)
    # <kind> to plant in <month>: <combined_list"
    if len(combined_list) > 0: 
        return f"{kind} to plant in {month}: {combined_list}."
    else: 
        return f"No {kind}s to plant in {month}."
