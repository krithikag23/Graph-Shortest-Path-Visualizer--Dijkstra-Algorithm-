# a_star_grid_animated.py

import heapq
import math

def heuristic(a, b):
    # Euclidean distance (best for diagonal movement)
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def get_neighbors(pos, grid):
    # 8-direction movement
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),     # straight
        (1, 1), (1, -1), (-1, 1), (-1, -1)    # diagonals
    ]

    rows, cols = len(grid), len(grid[0])
    neighbors = []

    for dx, dy in directions:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            # diagonal cost = √2, straight = 1
            cost = math.sqrt(2) if dx != 0 and dy != 0 else 1
            neighbors.append(((nx, ny), cost))

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

        for (neighbor, move_cost) in get_neighbors(current, grid):
            tentative = g_cost[current] + move_cost
            if neighbor not in g_cost or tentative < g_cost[neighbor]:
                g_cost[neighbor] = tentative
                f = tentative + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))
                parent[neighbor] = current

    return parent, visited


def reconstruct_path(parent, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent.get(goal)
    return path[::-1]
