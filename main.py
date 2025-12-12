# main.py

import json
from visualize import visualize_graph
from dijkstra import dijkstra, get_path
from a_star import a_star, reconstruct_path

# Load graph from JSON file
with open("graph_data.json") as f:
    graph = json.load(f)

print("Available nodes:", ", ".join(graph.keys()))

start = input("Enter start node: ").strip()
target = input("Enter target node: ").strip()

if start not in graph or target not in graph:
    print("Invalid nodes. Try again.")
    exit()

# ---------------------------
# Dijkstra Algorithm
# ---------------------------
distances, parent = dijkstra(graph, start)
path = get_path(parent, target)

print("\n--- Dijkstra Algorithm ---")
print("Path:", " -> ".join(path))
print("Cost:", distances[target])

# Visualize Dijkstra path
print("\nVisualizing Dijkstra shortest path...")
visualize_graph(graph, path)

# ---------------------------
# A* Algorithm
# ---------------------------
a_star_costs, a_star_parent = a_star(graph, start, target)
a_star_path = reconstruct_path(a_star_parent, target)

print("\n--- A* Algorithm ---")
print("Path:", " -> ".join(a_star_path))
print("Cost:", a_star_costs[target])

# Visualize A* path
print("\nVisualizing A* shortest path...")
visualize_graph(graph, a_star_path)
