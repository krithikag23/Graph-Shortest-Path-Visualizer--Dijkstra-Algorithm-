# compare_bfs_astar.py

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from grid import GRID, START, GOAL
from bfs_grid_animated import bfs_animated, reconstruct_path as bfs_path