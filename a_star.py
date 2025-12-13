# a_star.py

import heapq

def heuristic(a, b):
    return 1  # simple admissible heuristic


def a_star(graph, start, goal):
    open_set = [(0, start)]
    g_cost = {node: float("inf") for node in graph}
    g_cost[start] = 0

    parent = {node: None for node in graph}
    visited_count = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        visited_count += 1

        if current == goal:
            break

        for neighbor, weight in graph[current]:
            tentative = g_cost[current] + weight
            if tentative < g_cost[neighbor]:
                g_cost[neighbor] = tentative
                parent[neighbor] = current
                f_cost = tentative + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_cost, neighbor))

    return g_cost, parent, visited_count


def reconstruct_path(parent, target):
    path = []
    while target:
        path.append(target)
        target = parent[target]
    return path[::-1]
