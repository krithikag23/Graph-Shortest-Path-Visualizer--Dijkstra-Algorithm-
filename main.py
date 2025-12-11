# main.py

import json
from visualize import visualize_graph
from dijkstra import dijkstra, get_path
from a_star import a_star, reconstruct_path


with open("graph_data.json") as f:
    graph = json.load(f)

start = input("Enter start node: ").strip()
target = input("Enter target node: ").strip()

if start not in graph or target not in graph:
    print("Invalid nodes. Try again.")
    exit()

distances, parent = dijkstra(graph, start)
path = get_path(parent, target)

print("\nShortest path:", " -> ".join(path))
print("Total cost:", distances[target])

visualize_graph(graph, path)

# Run A* Algorithm
a_star_costs, a_star_parent = a_star(graph, start, target)
a_star_path = reconstruct_path(a_star_parent, target)

print("\n--- A* Algorithm ---")
print("Path:", " -> ".join(a_star_path))
print("Cost:", a_star_costs[target])
