#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plt

def de_bruijn_graph(string, k):
    """
    Generate nodes and edges for a de Bruijn graph from a given string.

    Parameters:
    - string (str): The input string.
    - k (int): The length of k-mers.

    Returns:
    - tuple: A tuple containing two elements:
             1. A set of nodes representing k-mers.
             2. A list of tuples representing edges between k-mers.
    """
        
    edges = []
    nodes = set()
    
    for i in range(len(string) - k + 1):
        edges.append((string[i:i+k-1], string[i+1:i+k])) #left and right k-mer
        nodes.add(string[i:i+k-1])
        nodes.add(string[i+1:i+k])
        
    return nodes, edges

def visualize_de_bruijn_graph(nodes, edges):
    """
    Visualizes a De Bruijn graph.

    Parameters:
        nodes (list): List of nodes in the graph.
        edges (list): List of edges in the graph, where each edge is represented as a tuple (u, v).

    Returns:
        None: This function displays the De Bruijn graph.
    """
    
    G = nx.DiGraph()
    G.add_nodes_from(nodes)

    # Create a new graph to include repeat edges
    H = nx.MultiDiGraph()
    for u, v in edges:
        H.add_edge(u, v)

    # Draw nodes
    pos = nx.spring_layout(H)
    nx.draw_networkx_nodes(H, pos, node_size=700, node_color='lightblue', label=nodes)

    # Draw edges
    edge_labels_drawn = set()  # to keep track of drawn edges
    for u, v in H.edges():
        edge_labels = H.get_edge_data(u, v)
        if (u, v) not in edge_labels_drawn:
            nx.draw_networkx_edges(H, pos, edgelist=[(u, v)], edge_color='gray', arrowsize=25, connectionstyle='arc3, rad=0.2')
            edge_labels_drawn.add((u, v))
        else:
            pos[u][1] += 0.08  # adjust y-position to avoid overlap
            nx.draw_networkx_edges(H, pos, edgelist=[(u, v)], edge_color='gray', arrowsize=25, connectionstyle='arc3, rad=0.2')

    # Draw labels
    nx.draw_networkx_labels(H, pos, font_size=15, font_weight="bold")

    plt.title("De Bruijn Graph")
    plt.show()
