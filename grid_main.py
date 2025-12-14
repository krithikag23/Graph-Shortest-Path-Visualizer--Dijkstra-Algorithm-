# grid_main.py

from grid import GRID, START, GOAL
from a_star_grid import a_star_grid, reconstruct_path
from visualize_grid import visualize_grid

parent = a_star_grid(GRID, START, GOAL)
path = reconstruct_path(parent, GOAL)

print("Grid Path:")
print(path)

visualize_grid(GRID, path)
