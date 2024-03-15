# Enchanted Forest Pathfinding

This repository contains a Python program simulating an adventurer's journey through the Enchanted Forest using the A* algorithm. The adventurer's objective is to find the hidden treasure while navigating through obstacles, wild animals, and restricted endpoints.

## Problem Description

The Enchanted Forest is represented by an 8x8 grid, where each cell represents a specific part of the forest. The adventurer begins at the northwest corner and must reach the treasure located at the southeast corner. The forest contains various elements such as safe grids, obstacles, the starting point, the goal, and endpoints.

## Implemented Algorithm: A* Search

The A* search algorithm is used to find the optimal path through the Enchanted Forest. A* combines the benefits of uniform cost search with a heuristic function to guide the search towards the goal efficiently. The Manhattan distance heuristic is employed to estimate the cost from the current position to the goal.

## How to Run the Program

To run the program:

1. Execute the Python script `A_star.py`.
2. Follow the instructions displayed in the GUI window to visualize the adventurer's journey and the minimum cost to reach the treasure.

## Dependencies

The program utilizes the following Python libraries:

- `tkinter`: For creating the graphical user interface (GUI) to visualize the Enchanted Forest grid.
- `PIL`: For image processing and displaying icons on the GUI.

## Code Structure

The code is structured as follows:

- `generate_random_grid()`: Function to generate a random grid representing the Enchanted Forest.
- `calculate_cost()`: Function to calculate the cost associated with each grid element.
- `move_adventurer()`: Function to move the adventurer within the grid.
- `heuristic()`: Function to calculate the Manhattan distance heuristic.
- `a_star()`: A* search algorithm implementation to find the optimal path.
- `draw_grid()`: Function to visualize the Enchanted Forest grid and the adventurer's journey.
- `main()`: Entry point of the program, where the Enchanted Forest simulation is initialized.

## Note

This implementation is designed to handle dynamic challenges such as probabilistic encounters with wild animals and restrictions posed by endpoints within the Enchanted Forest. Additionally, it aims to find the optimal path with minimal cost.

Enjoy your adventure through the Enchanted Forest!
