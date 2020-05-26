# Conway's Game of Life
Conway's Game of Life is a project that graphically displays a matrix containing alive and dead cells. The 
cells within the matrix evolve over generations according to a set of rules.

## Getting Started
#### Prerequisites
This project uses the following third-party modules:
* pygame
* ast
* pyperclip

To install these modules, type the following into terminal:
```
pip install pygame==2.0.0dev6
pip install ast
pip install pyperclip
```

## Background
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2) Any live cell with two or three live neighbours lives on to the next generation.
3) Any live cell with more than three live neighbours dies, as if by overpopulation.
4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

[...more info](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Features
#### Existing Grid
An existing one line matrix comprised of 1's and 0's can be pasted into the terminal to be used.

#### New Grid
A blank matrix with user inputted width and height will be displayed in the pygame window. The user can
determine whether each cell in the matrix is either alive or dead by pressing 1 or 0.

#### Number of Generations
The user can determine the number of generations to run the simulation for.

#### Generation Progression
The user can determine how the simulation will progress from one generation to the next.

Automatic - The user can determine the time delay between automatically progressing generations.

Manual - The user can determine when to progress to the next generation by pressing the ENTER key.

## Author
* **Michael Xu**






