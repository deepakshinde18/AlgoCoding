"""This program find the short path from start point to end point
    https://github.com/techwithtim/3-Mini-Python-Projects-For-Intermediates/blob/main/path-finder.py
"""

import curses
from curses import wrapper
import queue
import time


def print_maze(maze, stdscr, path=None):
    """Print the maze

    Args:
        maze (_type_): _description_
        stdscr (_type_): _description_
        path (list, optional): _description_. Defaults to [].
    """
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)


def find_start(maze, start):
    """find start point of Maze

    Args:
        maze (_type_): _description_
        start (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None


def find_path(maze, stdscr):
    """find shortest path and return

    Args:
        maze (_type_): _description_
        stdscr (_type_): _description_

    Returns:
        _type_: _description_
    """
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    print(start_pos)
    print([start_pos])

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, col):
    """_summary_

    Args:
        maze (_type_): _description_
        row (_type_): _description_
        col (_type_): _description_

    Returns:
        _type_: _description_
    """
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):
    """_summary_

    Args:
        stdscr (_type_): _description_
    """
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    maze = [
        ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "X", "#"],
    ]
    find_path(maze, stdscr)
    stdscr.getch()


wrapper(main)
