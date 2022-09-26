import networkx as nx

d=nx.Graph()#undirected
d.add_edge("Rajkot","Morbi")
d.add_edge("Morbi","Hadvad")
d.add_edge("Hadvad","Ahmd")
d.add_edge("Rajkot","Junagadh")
d.add_edge("Junagadh","Ahmd")
d.add_edge("Rajkot","jamnager")
d.add_edge("jamnager","Rajkot")
d.add_edge("Rajkot","Ahmd")
nx.draw(d,with_labels=True)

