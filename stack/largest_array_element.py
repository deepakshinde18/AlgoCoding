"""This function returns largest element from array"""
from pydantic import validate_call


@validate_call
def get_largest_array_element(data: list[int]):
    """function to return largest element from array

    Args:
        data (list): list of int
    """
    large = data[0]
    for i in data:
        if i > large:
            large = i
    return large


print(get_largest_array_element([4, 5, 6, 7, 1, 45, 23]))
