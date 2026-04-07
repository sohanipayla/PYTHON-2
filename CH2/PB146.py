import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
routes = [
    ("Kolkata", "Mumbai"), ("Mumbai", "Pune"), ("Mumbai", "Goa"),
    ("Kolkata", "Delhi"), ("Kolkata", "Bhubaneshwar"), ("Mumbai", "Delhi"),
    ("Delhi", "Chandigarh"), ("Delhi", "Surat"), ("Kolkata", "Hyderabad"),
    ("Hyderabad", "Chennai"), ("Chennai", "Thiruvananthapuram"),
    ("Thiruvananthapuram", "Hyderabad"), ("Kolkata", "Varanasi"),
    ("Delhi", "Varanasi"), ("Mumbai", "Bangalore"), ("Chennai", "Bangalore"),
    ("Hyderabad", "Bangalore"), ("Kolkata", "Guwahati")
]
G.add_edges_from(routes)
plt.figure(figsize=(15, 15))
nx.draw(G, 
        with_labels=True, 
        node_color='green', 
        node_size=3000, 
        edge_color='red', 
        arrowsize=20, 
        font_size=10, 
        font_weight='bold')

plt.title("Airlines Route Network Graph", fontsize=20)
plt.show()