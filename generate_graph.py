# generate_graph.py

import random
import json

def generate_graph(num_nodes=8, edge_prob=0.4, min_w=1, max_w=10):
    nodes = [chr(ord('A') + i) for i in range(num_nodes)]
    graph = {node: [] for node in nodes}

    for u in nodes:
        for v in nodes:
            if u != v and random.random() < edge_prob:
                weight = random.randint(min_w, max_w)
                graph[u].append([v, weight])

    return graph

def save_graph(graph, filename="graph_data.json"):
    with open(filename, "w") as f:
        json.dump(graph, f, indent=4)
    print(f"Graph saved to {filename}")