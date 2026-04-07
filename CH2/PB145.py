import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5])
edges = [(1,2),(1,3),(2,4),(3,5)]
G.add_edges_from(edges)
nx.draw(G,with_labels=True, node_color='lightblue', node_size=2000)
plt.title("Employee Social Network")
plt.show()