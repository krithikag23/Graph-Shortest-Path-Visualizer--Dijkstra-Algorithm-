# dijkstra.py

import heapq

def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    parent = {node: None for node in graph}

    pq = [(0, start)]
    visited_count = 0

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > dist[node]:
            continue

        visited_count += 1

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, parent, visited_count


def get_path(parent, target):
    path = []
    while target:
        path.append(target)
        target = parent[target]
    return path[::-1]
