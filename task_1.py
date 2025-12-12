import networkx as nx
import matplotlib.pyplot as plt

# 1. Генерація Графа
# n=20: кількість вершин
# k=4: кожен вузол з'єднаний з 4 найближчими сусідами (кільце)
# p=0.15: ймовірність, що дорога піде "навпростець" в інший кінець міста
G = nx.watts_strogatz_graph(n=20, k=4, p=0.15, seed=42)

mapping = {i: f"Stop {i+1}" for i in range(20)}
G = nx.relabel_nodes(G, mapping)

plt.figure(figsize=(10, 8))

pos = nx.kamada_kawai_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightgreen",
    node_size=800,
    font_size=9,
    edge_color="gray",
    width=1.5,
)
plt.title("Транспортна мережа (20 зупинок)")
plt.show()

print("-" * 40)
print(f"Кількість зупинок (вершин): {G.number_of_nodes()}")
print(f"Кількість маршрутів (ребер): {G.number_of_edges()}")
print("-" * 40)

print("Найважливіші вузли (найбільше доріг):")
degrees = dict(G.degree())
# топ-5
sorted_degrees = sorted(degrees.items(), key=lambda item: item[1], reverse=True)[:5]

for node, degree in sorted_degrees:
    print(f"{node}: {degree} доріг")
print("-" * 40)
