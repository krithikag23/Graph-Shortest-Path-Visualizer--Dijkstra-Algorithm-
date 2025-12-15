# grid_animate.py

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from grid import GRID, START, GOAL
from a_star_grid_animated import a_star_animated, reconstruct_path

parent, visited = a_star_animated(GRID, START, GOAL)
path = reconstruct_path(parent, GOAL)

rows, cols = len(GRID), len(GRID[0])
fig, ax = plt.subplots()

def draw(frame):
    ax.clear()
    ax.set_title("A* Grid Pathfinding (Animated)")

    # draw grid
    for i in range(rows):
        for j in range(cols):
            color = "black" if GRID[i][j] == 1 else "lightgray"
            ax.scatter(j, rows-i-1, c=color, s=300)

    # visited nodes
    for v in visited[:frame]:
        ax.scatter(v[1], rows-v[0]-1, c="blue", s=200)

    # final path
    if frame >= len(visited):
        x = [p[1] for p in path]
        y = [rows-p[0]-1 for p in path]
        ax.plot(x, y, c="green", linewidth=3)

    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.grid(True)
anim = FuncAnimation(
    fig,
    draw,
    frames=len(visited) + 8,
    interval=300,
    repeat=False
)

plt.show()