# a_star_grid_animated.py

import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(pos, grid):
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    rows, cols = len(grid), len(grid[0])
    neighbors = []

    for dx, dy in moves:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors