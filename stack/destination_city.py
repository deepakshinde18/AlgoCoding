"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there
exists a direct path going from cityAi to cityBi.
Return the destination city, that is,
the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which
is the destination city. Your trip consist of:
"London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
"""

from typing import List


def destcity(paths: List[List[str]]) -> str:
    """_summary_

    Args:
        paths (List[List[str]]): path list

    Returns:
        str: destn
    """
    starts = {i[0] for i in paths}

    for i in paths:
        if i[1] not in starts:
            starts.clear()
            paths.clear()
            return i[1]
    return None


print(destcity([["B", "C"], ["D", "B"], ["C", "A"]]))
