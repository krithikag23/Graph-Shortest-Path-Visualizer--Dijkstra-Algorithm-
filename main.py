# main.py

import json
from visualize import visualize_graph
from dijkstra import dijkstra, get_path

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