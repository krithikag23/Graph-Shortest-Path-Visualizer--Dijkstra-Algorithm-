# a_star.py

import heapq
from math import sqrt

def heuristic(a, b):
    """Simple heuristic: Euclidean distance between node labels if numeric.
       If not numeric, return 1 (fallback)."""
    try:
        return abs(int(a) - int(b))
    except:
        return 1  # Fallback heuristic for non-numeric labels

def a_star(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))

    g_cost = {node: float("inf") for node in graph}
    g_cost[start] = 0

    f_cost = {node: float("inf") for node in graph}
    f_cost[start] = heuristic(start, goal)

    parent = {node: None for node in graph}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            break

        for neighbor, weight in graph[current]:
            tentative_g = g_cost[current] + weight

            if tentative_g < g_cost[neighbor]:
                parent[neighbor] = current
                g_cost[neighbor] = tentative_g
                f_cost[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_cost[neighbor], neighbor))

    return g_cost, parent

def reconstruct_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return list(reversed(path))    