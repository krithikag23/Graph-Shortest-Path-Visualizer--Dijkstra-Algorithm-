# compare_bfs_astar.py

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from grid import GRID, START, GOAL
from bfs_grid_animated import bfs_animated, reconstruct_path as bfs_path
from a_star_grid_animated import a_star_animated, reconstruct_path as astar_path

# Run BFS and A*
bfs_parent, bfs_visited = bfs_animated(GRID, START, GOAL)
astar_parent, astar_visited = a_star_animated(GRID, START, GOAL)

bfs_final = bfs_path(bfs_parent, GOAL)
astar_final = astar_path(astar_parent, GOAL)

rows, cols = len(GRID), len(GRID[0])
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

def draw(ax, visited, path, title, frame):
    ax.clear()
    ax.set_title(title)

    for i in range(rows):
        for j in range(cols):
            color = "black" if GRID[i][j] == 1 else "lightgray"
            ax.scatter(j, rows-i-1, c=color, s=300)

    for v in visited[:frame]:
        ax.scatter(v[1], rows-v[0]-1, c="blue", s=180)

    if frame >= len(visited):
        x = [p[1] for p in path]
        y = [rows-p[0]-1 for p in path]
        ax.plot(x, y, c="green", linewidth=3)

    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.grid(True)
