# visualize_grid.py

import matplotlib.pyplot as plt

def visualize_grid(grid, path):
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                plt.scatter(j, rows-i-1, c="black", s=300)
            else:
                plt.scatter(j, rows-i-1, c="lightgray", s=300)

    if path:
        x = [p[1] for p in path]
        y = [rows - p[0] - 1 for p in path]
        plt.plot(x, y, c="green", linewidth=3)

    plt.title("Grid-Based Pathfinding (A*)")
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.grid(True)
    plt.show()
