# a_star_grid_animated.py

import heapq
import math

def heuristic(a, b):
    # Euclidean distance (best for diagonal movement)
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def get_neighbors(pos, grid):
    import math

    rows, cols = len(grid), len(grid[0])
    x, y = pos

    # (dx, dy, cost)
    directions = [
        (0, 1, 1), (1, 0, 1), (0, -1, 1), (-1, 0, 1),      # straight
        (1, 1, math.sqrt(2)), (1, -1, math.sqrt(2)),      # diagonals
        (-1, 1, math.sqrt(2)), (-1, -1, math.sqrt(2))
    ]

    neighbors = []

    for dx, dy, cost in directions:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < rows and 0 <= ny < cols):
            continue

        if grid[nx][ny] == 1:
            continue

        # 🚫 Prevent diagonal corner cutting
        if dx != 0 and dy != 0:
            if grid[x + dx][y] == 1 or grid[x][y + dy] == 1:
                continue

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
