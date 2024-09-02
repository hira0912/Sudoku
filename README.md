# This Program Purpose
This program is for solving Sudoku.
The execution environment uses AWS Lambda and is executed using the python language.

# Program List
## Sudoku01.py
The purpose of this program is to solve Sudoku problems. 

Created based on the claim that all cells can be placed by deriving the placement possibilities of each cell and continuing the process of filling in the finalized cells (the number that can be placed in the target cell can be specified). I'm doing it.

However, it was found that the board surface that could not be specified occurred for all empty cells on the board surface, and it was found that this program was not perfect.


## Sudoku02.py
The purpose of this program is to derive the answer to Sudoku through a complete search.
By checking all the patterns created by the recursive function after creation, it is possible to confirm whether the patterns are appropriate and output patterns that have no problems.

However, we found that this program was extremely slow, and took so long that it violated AWS Lambda's execution time limit, especially on boards with many empty cells.


## Sudoku03-1.py
This is a program that solves Sudoku using the DFS (depth-first search) method.
This allows you to solve very complex Sudoku quickly. However, there are some improvements that could be made, so we decided to add them.


## Sudoku03-2.py
Based on Sudoku03-1, the idea/function of Sudoku01 has been added.

Specifically, before assuming a cell in DFS and searching for the possibility of placing the next cell, the assumption of the cell's numerical value influences the search for other confirmed cells, and Added processing to fill the space.

Additionally, we have also added a process that breaks the process if there is a cell in which all numerical values ​​cannot be placed due to the influence of assumptions.

### Added Function
- organize_panel

This Function is based Sudoku01. 

## Sudoku03-3.py
This is a program that has been improved upon Sudoku03-2.

When I ran Sudoku03-2, the number of assumed placement steps was significantly reduced, but the execution time was not reduced commensurately. I thought this was because the execution rate of the added function (organize_panel) was constant, and this execution process was hindering speed improvement.

To improve this, until now the order of cell placement was to follow all cells in order from the top left to the right, but we have added a process to skip when the next cell is full. This greatly reduced the number of times the function (organize_panel) was executed, improving speed.

### Added Function
- next_position

This Function is solved next step position for dfs.

### Changed Structure
Changed the placement possibility used for DFS from list to queue.
This is because we thought it would be faster since it only performs FIFO (First-In First-Out), but since the original array was not large, the effect was small.