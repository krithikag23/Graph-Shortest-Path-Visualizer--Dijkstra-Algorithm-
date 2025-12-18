# compare_bfs_astar.py

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from grid import GRID, START, GOAL
from bfs_grid_animated import bfs_animated, reconstruct_path as bfs_path
from a_star_grid_animated import a_star_animated, reconstruct_path as astar_path

# Run BFS and A*
bfs_parent, bfs_visited = bfs_animated(GRID, START, GOAL)
astar_parent, astar_visited = a_star_animated(GRID, START, GOAL)