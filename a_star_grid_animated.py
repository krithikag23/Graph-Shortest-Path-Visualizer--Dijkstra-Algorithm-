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

def a_star_animated(grid, start, goal):
    open_set = [(0, start)]
    g_cost = {start: 0}
    parent = {start: None}
    visited = []

    while open_set:
        _, current = heapq.heappop(open_set)
        visited.append(current)

        if current == goal:
            break

        for neighbor in get_neighbors(current, grid):
            new_cost = g_cost[current] + 1
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))
                parent[neighbor] = current

    return parent, visited