# bfs_grid_animated.py

from collections import deque

def get_neighbors(pos, grid):
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    rows, cols = len(grid), len(grid[0])
    neighbors = []

    for dx, dy in moves:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

def bfs_animated(grid, start, goal):
    queue = deque([start])
    parent = {start: None}
    visited_order = []

    while queue:
        current = queue.popleft()
        visited_order.append(current)

        if current == goal:
            break

        for neighbor in get_neighbors(current, grid):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return parent, visited_order
