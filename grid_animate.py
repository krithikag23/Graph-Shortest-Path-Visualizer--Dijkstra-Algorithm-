# grid_animate.py

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from grid import GRID, START, GOAL
from a_star_grid_animated import a_star_animated, reconstruct_path

parent, visited = a_star_animated(GRID, START, GOAL)
path = reconstruct_path(parent, GOAL)

rows, cols = len(GRID), len(GRID[0])
fig, ax = plt.subplots()