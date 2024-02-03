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

# Exemple de labyrinthe représenté par un graphe (dictionnaire)
labyrinthe = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B'],
    'D': ['A', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['E']
}

def afficher_graphe(graph):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_size=8)
    plt.show()

def afficher_chemin(graph, chemin):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_size=8)

    edges = [(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)

    plt.show()

afficher_graphe(labyrinthe)

start_node = 'A'
end_node = 'F'

resultat = calc_labyrinthe(labyrinthe, start_node, end_node)

if resultat:
    afficher_chemin(labyrinthe, resultat)
else:
    print(f"Aucun chemin trouvé de {start_node} à {end_node}")
