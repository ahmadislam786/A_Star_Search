#A_star Algorithm 
import random
import heapq
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

SAFEGRID = 0
OBSTACLE = -1
START = 2
GOAL = 3
ENDPOINT = 5

GRID_SIZE = 8

ELEMENT_NAMES = {SAFEGRID: 'Safe', OBSTACLE: 'Obstacle', START: 'Start', GOAL: 'Goal', ENDPOINT: 'Endpoint'}

COLORS = {
    SAFEGRID: "#C8E6C9",
    START: "yellow"
}

ICONS = {
    OBSTACLE: "obstacle.jpeg",
    GOAL: "treasure.png"
}

#generate random grid wiht start and goal state fix
def generate_random_grid():
    grid = [[SAFEGRID for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    grid[0][0] = START
    grid[GRID_SIZE - 1][GRID_SIZE - 1] = GOAL

    for _ in range(GRID_SIZE // 2):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if grid[x][y] == SAFEGRID:
            grid[x][y] = OBSTACLE

    for _ in range(GRID_SIZE // 4):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if grid[x][y] == SAFEGRID:
            grid[x][y] = ENDPOINT

    return grid

#calculate the cost according to the element
def calculate_cost(element):
    if element == SAFEGRID:
        return random.randint(-3, -1)
    elif element == OBSTACLE:
        return random.randint(-4, -2)
    elif element == ENDPOINT:
        return -1
    elif element == GOAL:
        return 0
    else:
        return 0  # Default case


def move_adventurer(grid, x, y, direction):
    if direction == 'up':
        new_x, new_y = x - 1, y
    elif direction == 'down':
        new_x, new_y = x + 1, y
    elif direction == 'left':
        new_x, new_y = x, y - 1
    elif direction == 'right':
        new_x, new_y = x, y + 1

    if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
        new_cost = calculate_cost(grid[new_x][new_y])
        return new_x, new_y, new_cost
    else:
        return x, y, float('inf')


def heuristic(current, goal):
    """
    Calculates the Manhattan distance heuristic between the current position and the goal.
    """
    return abs(goal[0] - current[0]) + abs(goal[1] - current[1])


def a_star(grid):
    start = (0, 0)
    goal = (GRID_SIZE - 1, GRID_SIZE - 1)
    frontier = [(0 + heuristic(start, goal), start, 0)]  # Priority queue with (total_cost + heuristic, position, cumulative_cost)
    visited = set()
    path = {}

    while frontier:
        total_cost, (x, y), cumulative_cost = heapq.heappop(frontier)
        if (x, y) == goal:
            return cumulative_cost, path

        if (x, y) not in visited:
            visited.add((x, y))
            path[(x, y)] = (cumulative_cost, total_cost - heuristic((x, y), goal))

            for direction in ['up', 'down', 'left', 'right']:
                new_x, new_y, action_cost = move_adventurer(grid, x, y, direction)
                new_cumulative_cost = cumulative_cost + action_cost
                heapq.heappush(frontier, (new_cumulative_cost + heuristic((new_x, new_y), goal), (new_x, new_y), new_cumulative_cost))

    return float('inf'), path


def draw_grid(root, grid, min_cost, path):
    icon_size = 30
    icon_padding = 2
    path_color = "#388E3C"

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell_value = grid[i][j]
            color = COLORS.get(cell_value, "white")

            if (i, j) in path:
                color = path_color

            if cell_value in ICONS:
                icon_path = ICONS[cell_value]
                img = Image.open(icon_path)
                img = img.resize((icon_size, icon_size))

                icon = ImageTk.PhotoImage(img)
                label = tk.Label(root, image=icon, bg=color, borderwidth=1, relief="solid")
                label.image = icon
                label.grid(row=i, column=j, padx=icon_padding, pady=icon_padding)  # Adjust padding
            else:
                # Use text label
                label = tk.Label(root, text=ELEMENT_NAMES[cell_value], bg=color, width=8, height=2, borderwidth=1,
                                 relief="solid", font=("Arial", 10))
                label.grid(row=i, column=j, padx=2, pady=2)

    min_cost_label = tk.Label(root, text=f"A Star Minimum cost: {min_cost}", font=("Arial", 12))
    min_cost_label.grid(row=GRID_SIZE, columnspan=GRID_SIZE, padx=10, pady=10)


def main():
    grid = generate_random_grid()

    print("Forest Grid:")
    for row in grid:
        print(row)

    min_cost, path = a_star(grid)

    if min_cost == float('inf'):
        messagebox.showinfo("Pathfinding", "Unable to reach the goal.")
    else:
        messagebox.showinfo("Pathfinding", f"Minimum cost to reach the treasure: {min_cost}")

    # Create the GUI
    root = tk.Tk()
    root.title("Forest Grid")
    draw_grid(root, grid, min_cost, path)
    root.mainloop()


if __name__ == "__main__":
    main()