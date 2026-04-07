import matplotlib.pyplot as plt
import networkx as nx
plt.figure(figsize=(5,5))
g=nx.DiGraph()
g.add_nodes_from(range(0,6))
g.add_edges_from([(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(1,5),(2,0),(2,1),(2,4),(2,5)])
nx.draw_networkx(g, node_size=1000, node_color='pink', edge_color='black')
plt.show()