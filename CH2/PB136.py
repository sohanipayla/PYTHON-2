import matplotlib.pyplot as plt
import networkx as nx
plt.figure(figsize=(5,5))
g = nx.DiGraph()
g.add_nodes_from(['A', 'B', 'C', 'D'])
g.add_edges_from([('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'A')])
nx.draw_networkx(g, node_size=1000, node_color='lightblue', edge_color='black')
plt.show()