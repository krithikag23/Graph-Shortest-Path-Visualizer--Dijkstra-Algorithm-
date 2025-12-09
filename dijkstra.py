# dijkstra.py

import heapq

def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)
    parent = {node: None for node in graph}

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, parent
