import networkx as nx
import random

# граф
G = nx.watts_strogatz_graph(n=20, k=4, p=0.15, seed=42)
mapping = {i: f"Stop {i+1}" for i in range(20)}
G = nx.relabel_nodes(G, mapping)

# вага
for u, v in G.edges():
    weight = random.randint(1, 10)
    G[u][v]["weight"] = weight

print("Граф зважено. Випадкові відстані додано.\n")

# реалізація
lengths, paths = nx.single_source_dijkstra(G, source="Stop 1")

print(f"{'Куди':<10} | {'Час (хв)':<10} | {'Маршрут'}")
print("-" * 50)

for target in lengths:
    if target != "Stop 1":
        print(f"{target:<10} | {lengths[target]:<10} | {paths[target]}")

# приклад
start = "Stop 1"
end = "Stop 10"
print("-" * 50)
print(f"Найшвидший маршрут з {start} до {end}:")
print(f"Шлях: {paths[end]}")
print(f"Загальний час: {lengths[end]} хв")
