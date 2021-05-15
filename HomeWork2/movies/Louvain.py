# Homework#2 6 a)
#
# This Script was inspired by the folowing tutorial
# https://medium.com/analytics-vidhya/implement-louvain-community-detection-algorithm-using-python-and-gephi-with-visualization-871250fb2f25
# https://python-louvain.readthedocs.io/en/latest/api.html
# https://python-louvain.readthedocs.io/en/latest/
# https://github.com/taynaud/python-louvain
#



from typing import Counter
import networkx as nx
import community as community_louvain
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from networkx.linalg.modularitymatrix import modularity_matrix
COLOR = '#40a6d1'


print("Network Science Louvain Algorithm HW#2: ")

# Getting all the datasets in teh directory

# only on linux based systems
#list=os.system("ls")
#list2=list.split()

#print(list)


# Read the graph

#file="starwars_v.gml"
#file="pulp_fiction.gml"
#file="bladerunner.gml"
#file="godfather_ii.gml"
file="lordrings_returnking.gml"

G=nx.read_gml(file)

#G=nx.karate_club_graph()

nx.draw(G, alpha = 0.3, edge_color = COLOR, node_color = COLOR, node_size=50)
plt.show()


# Louvain Algorithm
partition = community_louvain.best_partition(G)

# visualization
pos = nx.spring_layout(G)
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=100,cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()

#print(partition.values())


#Graph properties:
print(file) #Name
print("nodes: ",G.number_of_nodes()) #N nodes
print("edges: ",G.number_of_edges()) #N edges

# Louvain communities:

#print(Counter(partition.values()))
print("Number of communities ", len(Counter(partition.values())))

# Modularity:
print("Modularity of the community: ",community_louvain.modularity(partition,G))





#é possível fazer um dendograma
#>>> G=nx.erdos_renyi_graph(100, 0.01)
#>>> dendrogram = generate_dendrogram(G)
#>>> for level in range(len(dendrogram) - 1) :
#>>>     print("partition at level", level, "is", partition_at_level(dendrogram, level))  # NOQA

