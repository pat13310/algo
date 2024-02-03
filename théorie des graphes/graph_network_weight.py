import networkx as nx
import matplotlib.pyplot as plt

def calc_labyrinthe(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = calc_labyrinthe(graph, neighbor, end, path)
            if new_path:
                return new_path

    return None

# Exemple de labyrinthe représenté par un graphe (dictionnaire) avec des poids
labyrinthe_poids = {
    'A': {'B': 1, 'D': 2},
    'B': {'A': 1, 'C': 3, 'E': 4},
    'C': {'B': 3},
    'D': {'A': 2, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 5},
    'F': {'E': 5}
}

def afficher_graphe(graph):
    G = nx.Graph()

    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def afficher_chemin(graph, chemin):
    G = nx.Graph()

    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    edges = [(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)

    plt.show()

afficher_graphe(labyrinthe_poids)

start_node = 'A'
end_node = 'F'

resultat = calc_labyrinthe(labyrinthe_poids, start_node, end_node)

if resultat:
    afficher_chemin(labyrinthe_poids, resultat)
else:
    print(f"Aucun chemin trouvé de {start_node} à {end_node}")
