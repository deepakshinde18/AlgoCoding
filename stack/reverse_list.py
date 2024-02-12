"""
This module is created to reverse given list
"""

from pydantic import validate_call


@validate_call
def reverse_list(data: list[int | str]) -> list[int | str]:
    """
    Args:
        data (list[int | str]): list to reverse

    Returns:
        list[int|str]: retrun reversed list
    """
    left = 0
    right = len(data) - 1
    while left < right:
        temp = data[right]
        data[right] = data[left]
        data[left] = temp
        left += 1
        right -= 1
    return data


print(reverse_list(["p", "r", "e", "p", "b", "y", "t", "e", "s"]))
print(reverse_list([3, "r", 4, "p", "b", "y", "t", "e", "s"]))
