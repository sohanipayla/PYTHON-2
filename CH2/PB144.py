import matplotlib.pyplot as plt
import networkx as nx
plt.figure(figsize=(5,5))
g=nx.DiGraph()
g.add_nodes_from(range(0,5))
g.add_edges_from([(0,1),(0,2),(0,4),(1,2),(1,4),(2,0),(2,1),(2,3),(2,4),(3,0),(3,1),(3,2),(4,0),(4,1)])
nx.draw_networkx(g, node_size=1000, node_color='pink', edge_color='blue')
plt.show()