"""
Module to return index of element whose sum is target
"""


def two_sum(nums, target):
    """_summary_

    Args:
        nums (_type_): _description_
        target (_type_): _description_

    Returns:
        _type_: _description_
    """
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [num_map[(target - num)], i]
        num_map[num] = i
    return None


print(two_sum([2, 7, 11, 15], 9))
