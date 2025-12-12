import networkx as nx

# граф
G = nx.watts_strogatz_graph(n=20, k=4, p=0.15, seed=42)
mapping = {i: f"Stop {i+1}" for i in range(20)}
G = nx.relabel_nodes(G, mapping)

# точки маршруту
start_node = "Stop 1"
end_node = "Stop 10"

print(f"шлях від {start_node} до {end_node}...\n")

# DFS (Пошук у глибину)
dfs_tree = nx.dfs_tree(G, source=start_node)
dfs_path = list(nx.shortest_path(dfs_tree, source=start_node, target=end_node))

print(f"DFS (У глибину): {dfs_path}")
print(f"довжина шляху DFS: {len(dfs_path) - 1} кроків")
print("-" * 40)

# BFS
bfs_path = list(nx.shortest_path(G, source=start_node, target=end_node))

print(f"BFS (У ширину):  {bfs_path}")
print(f"Довжина шляху BFS: {len(bfs_path) - 1} кроків")
print("-" * 40)
