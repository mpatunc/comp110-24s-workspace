"""Functions that implement sorting algorithms."""

__author__ = "730602218"


def insertion_sort(list2: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list"""
    counter = 0 
    while counter < len(list2): 
        min_index = counter
        for i in range(counter + 1, len(list2)):
            if list2[i] < list2[min_index]:
                min_index = i 
        if min_index != counter: 
            list2[counter], list2[min_index] = list2[min_index], list2[counter]
        counter += 1
    return None

# index
    # sort_idx: int = 0 
    # # loop to find min
    # while sort_idx < len(list2) - 1: 
    #     unsort_idx : int = sort_idx + 1
    #     cur_elem = list2[unsort_idx]
    #     # replace using the same structure as selection_sort
    #     while unsort_idx > 0 and cur_elem < list2[unsort_idx - 1]:
    #         temp_num = list2[unsort_idx]
    #         list2[unsort_idx] = list2[unsort_idx - 1]
    #         list2[unsort_idx - 1] = temp_num
    #         unsort_idx -= 1
    #     sort_idx += 1 


def selection_sort(list1: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    for i in range(1, len(list1)): 
        current_element = list1[i]
        j = i - 1
        while j >= 0 and list1[j] > current_element: 
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = current_element
    return None  


# counter: int = 0 
    # # loop through list and find the min
    # while counter < len(list1): 
    #     min_elem = counter
    #     counter2 = counter 
    #     while counter2 < len(list1): 
    #         if list1[counter2] < list1[min_elem]: 
    #             min_elem = counter2
    #         counter2 += 1
    # # replace counter with min needs to outside while loop
    #     if min_elem != counter: 
    #         temp_int = list1[counter]
    #         list1[counter] = list1[min_elem]
    #         list1[min_elem] = temp_int
    #     counter += 1