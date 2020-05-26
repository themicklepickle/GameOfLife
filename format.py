# Project - Conway's Game of Life
# Functions to format matrices
# Michael Xu
# May 19, 2020


# pyperclip module to copy strings to clipboard
import pyperclip


def to_grid(matrix):
    """
    Formats a matrix as a grid.
    Prints the grid and copies it to clipboard.
    
    Args:
        matrix (matrix): two dimensional list

    Returns:
        None

    Example:
        >>> to_grid([[0, 1, 1], [0, 0, 1], [1, 1, 1]])
        [[0, 1, 1],
         [0, 0, 1],
         [1, 1, 1]]
    """
    grid = str(matrix).split("],")
    grid = "],\n".join(grid)
    pyperclip.copy(grid)
    print(grid)


def to_list(grid):
    """
    Formats a grid as a one-line matrix.
    Prints the matrix and copies it to clipboard.

    Args:
        grid (matrix): two dimensional list

    Returns:
        None

    Example:
        >>> to_grid([[0, 1, 1],
                     [0, 0, 1],
                     [1, 1, 1]])
        [[0, 1, 1], [0, 0, 1], [1, 1, 1]]
    """
    pyperclip.copy(str(grid))
    print(grid)


def blank_grid(width, height):
    """
    Creates a grid filled with 0.
    Prints the grid and copies it to clipboard.

    Args:
        width (int): width of grid
        height (int): height of grid

    Returns:
        None

    Example:
        >>> blank_grid(3, 3)
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    """
    blank = f"[{[0] * width},\n" + f" {[0] * width},\n" * (height - 2) + f" {[0] * width}]"
    pyperclip.copy(blank)
    print(blank)
