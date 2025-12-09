# main.py

import json
from dijkstra import dijkstra, get_path

with open("graph_data.json") as f:
    graph = json.load(f)

start = input("Enter start node: ").strip()
target = input("Enter target node: ").strip()

if start not in graph or target not in graph:
    print("Invalid nodes. Try again.")
    exit()

distances, parent = dijkstra(graph, start)