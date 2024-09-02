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


## Sudoku04-1.py
This is a program with a modified structure of Sudoku03-1.

In terms of directionality, we attempted to dynamically change the order of execution, which had previously been executed sequentially from the top left cell to the right. We thought that cells that are processed in the early stages have a high possibility of placement, that is, cells that have fewer branches will have higher processing efficiency.

Therefore, we considered improving efficiency by calculating the placement possibilities of all cells each time, and selecting cells with the highest placement possibility as assumptions in order.
However, the speed was actually significantly lower than Sudoku03-1. This is due to the high rate at which placement possibilities are calculated.

### Added Function
- calc_next_position

This Function is solved next step position for dfs.

The name is similar to the function added in Sudoku03-3, but whereas Sudoku03-3 simply determines whether the next cell is empty, this function calculates the placement possibility of all cells.

The specification is to select the most appropriate cell for the next calculation from among them.
However, each time it is executed, a calculation amount of O(24K) when the number of empty cells is K is generated, so there is a possibility that the speed will be extremely slow.

### Changed Structure
As mentioned in the overview, we changed the assumed order of cells.


## Sudoku04-2.py
Based on Sudoku04-1, the idea/function of Sudoku01 has been added.The idea is the same as what was added in Sudoku03-2, so I will not explain the overview of Sudoku01 here (see the overview of Sudoku03-2)

However, we found that even with this method added, the results were much slower than Sudoku03-1. This shows that increasing the number of trials assumed for DFS was faster than dynamically optimizing placement possibilities.

There is a possibility that if this method is improved further, it may be faster than the Sudoku03 series, but as it is currently not very likely, we have decided not to pursue it any further.
