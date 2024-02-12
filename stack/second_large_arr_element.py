"""
This function returns second largest element from array
"""

from pydantic import validate_call


@validate_call
def second_largest_element(data: list[int]):
    """
    This is brute force implementation to get second largest
    element from array

    Args:
        data (list[int]): list of int to get second largest element
    """
    sorted_data = sorted(data)
    largest = sorted_data[-1]
    for i in reversed(sorted_data):
        if i != largest:
            return i
    return -1


print(second_largest_element([4, 5, 6, 7, 1, 45, 23]))


@validate_call
def second_largest_element_optimal(data: list[int]):
    """
    This is the optimal solution to get second largest
    element from array

    Args:
        data (list[int]): list of int to get second largest element
    """
    largest = data[0]
    s_largest = float("-inf")
    for i in data:
        if i > largest:
            s_largest = largest
            largest = i
        elif s_largest < i < largest:
            s_largest = i
    return s_largest


print(second_largest_element_optimal([4, 5, 6, 7, 1, 45, 23]))
