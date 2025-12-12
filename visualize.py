# visualize.py

import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, path=None, title="Graph Visualization"):
    G = nx.DiGraph()

    # Add nodes and weighted edges
    for node, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)  # consistent layout

    # Draw nodes
    nx.draw_networkx_nodes(
        G, pos, node_size=800, node_color="#90c3f9", edgecolors="black"
    )

    # Draw edges
    normal_edges = []
    path_edges = set(zip(path, path[1:])) if path else set()

    for u, v in G.edges():
        if (u, v) in path_edges:
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=3, edge_color="green")
        else:
            normal_edges.append((u, v))

    nx.draw_networkx_edges(G, pos, edgelist=normal_edges, width=1.5, edge_color="black")

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    # Draw weights on edges
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(title)
    plt.axis("off")
    plt.show()


def visualize_comparison(graph, dijkstra_path, astar_path):
    G = nx.DiGraph()

    for node, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_size=800, node_color="#90c3f9", edgecolors="black")

    # Dijkstra edges - green
    dij_edges = set(zip(dijkstra_path, dijkstra_path[1:]))

    # A* edges - red
    ast_edges = set(zip(astar_path, astar_path[1:]))

    # Normal edges
    normal = []

    for u, v in G.edges():
        if (u, v) in dij_edges:
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=3, edge_color="green", label="Dijkstra")
        elif (u, v) in ast_edges:
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=3, edge_color="red", label="A*")
        else:
            normal.append((u, v))

    nx.draw_networkx_edges(G, pos, edgelist=normal, width=1.5, edge_color="black")

    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    green_patch = plt.Line2D([0], [0], color="green", lw=3, label="Dijkstra Path")
    red_patch = plt.Line2D([0], [0], color="red", lw=3, label="A* Path")

    plt.legend(handles=[green_patch, red_patch])
    plt.title("Dijkstra vs A* Path Comparison")
    plt.axis("off")
    plt.show()
