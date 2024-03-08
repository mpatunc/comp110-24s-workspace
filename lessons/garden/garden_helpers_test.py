"""Test my garden functions."""

__author__ = "730602218"

from lessons.garden.garden_helpers import add_by_kind 
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


# edge case for add by kind
def test_add_by_kind_format() -> None:
    """Format is correct when adding new plant type and plant or adding to."""
    new_plant_kind: str = "flower"
    new_plant: str = "marigold"
    test: dict[str, list[str]] = {}
    assert add_by_kind(test, new_plant_kind, new_plant) == test[new_plant_kind].append(new_plant)


# # use case for add by kind 
def test_add_by_kind_empty(): 
    """Dictionary added is empty."""
    new_plant_kind: str = ""
    new_plant: str = ""
    test: dict[str, list[str]] = {}
    assert add_by_kind(test, new_plant_kind, new_plant) == test[new_plant_kind].append(new_plant)


# edge case for add by date
def test_add_by_date_format() -> None: 
    """Format is correct when adding new month and plant or adding to."""
    month: str = "March"
    plant: str = "apple"
    test: dict[str, list[str]] = {}
    assert add_by_date(test, month, plant) == test[month].append(plant)


# use case for add by date
def test_add_by_date_empty() -> None:
    """Adding empty dictionary."""
    month: str = ""
    plant: str = ""
    test: dict[str, list[str]] = {}
    assert add_by_date(test, month, plant) == test[month].append(plant)


# use case for lookup_by_kind_and_date
def test_lookup_by_kind_and_date_output() -> None: 
    """Output for lookup_by_kind_and_date is acceptable."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "rose", "daisy"]}
    plants_by_month: dict[str, list[str]] = {"March": ["marigold", "rose", "daisy"]}
    kind: str = "flower"
    month: str = "March"
    combined_list: list[str] = ["marigold", "rose", "daisy"]
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_month, kind, month) == f"{kind} to plant in {month}: {combined_list}."


# edge case for lookup_by_kind_and_date
def test_lookup_by_kind_and_date_none() -> None: 
    """Output for lookup_by_kind_and_date if none to plant."""
    plants_by_kind: dict[str, list[str]] = {"fruit": []}
    plants_by_month: dict[str, list[str]] = {"March": []}
    kind: str = "fruit"
    month: str = "March"
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_month, kind, month) == f"No {kind}s to plant in {month}."