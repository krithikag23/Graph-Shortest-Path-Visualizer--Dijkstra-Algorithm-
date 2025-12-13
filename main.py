import time

# Dijkstra benchmark
start_time = time.time()
distances, parent, dijkstra_visits = dijkstra(graph, start)
dijkstra_time = time.time() - start_time
dijkstra_path = get_path(parent, target)

# A* benchmark
start_time = time.time()
a_costs, a_parent, astar_visits = a_star(graph, start, target)
astar_time = time.time() - start_time
astar_path = reconstruct_path(a_parent, target)

print("\n--- Benchmark Results ---")
print(f"Dijkstra Path: {' -> '.join(dijkstra_path)}")
print(f"Cost: {distances[target]}")
print(f"Nodes Visited: {dijkstra_visits}")
print(f"Time Taken: {dijkstra_time:.6f} seconds")

print("\nA* Path:", " -> ".join(astar_path))
print(f"Cost: {a_costs[target]}")
print(f"Nodes Visited: {astar_visits}")
print(f"Time Taken: {astar_time:.6f} seconds")
