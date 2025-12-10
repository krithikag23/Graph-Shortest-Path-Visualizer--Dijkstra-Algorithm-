import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, path=None):
    G = nx.DiGraph()

    # Add nodes and weighted edges
    for node, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # automatic positioning

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=800, node_color="skyblue")

    # Draw edges
    edge_colors = []
    for u, v in G.edges():
        if path and (u, v) in zip(path, path[1:]):
            edge_colors.append("green")  # highlight path edges
        else:
            edge_colors.append("black")

    nx.draw_networkx_edges(G, pos, width=2, edge_color=edge_colors)

    # Add labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    # Add edge weight labels
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Graph Visualization (Dijkstra Shortest Path)")
    plt.axis("off")
    plt.show()