import networkx as nx
import matplotlib.pyplot as plt
instagram = {
    'person1': [0, 1, 1, 0, 1],
    'person2': [0, 0, 1, 0, 1],
    'person3': [1, 1, 0, 1, 1],
    'person4': [1, 1, 1, 0, 0],
    'person5': [1, 1, 0, 0, 0]
}
plt.figure(figsize=(6,6))
G = nx.DiGraph()
node = list(instagram.keys())
G.add_nodes_from(node)
follow=list(instagram.values())
for i in range(len(instagram)):
    for j in range(len(instagram)):
        if follow[i][j] == 1:
            G.add_edge(node[i], node[j])
nx.draw_networkx(G,node_size=2500,node_color='pink',width=2,edge_color='black')
plt.show()