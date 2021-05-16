# Homework#2 6 c)




import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
from modularity_maximization import partition
from modularity_maximization.utils import get_modularity
COLOR = '#40a6d1'



#Files with the movies network
file="bladerunner.gml"
#file="starwars_v.gml"

G=nx.read_gml(file)

#nx.draw(G, alpha = 0.3, edge_color = COLOR, node_color = COLOR, node_size=50)
#plt.show()



# Louvain Algorithm
partition = community_louvain.best_partition(G)
#print(partition)

# Adjacency Matrix
A = nx.adjacency_matrix(G)
#print(A)

movie_modularity=0;

#for i in range(G.number_of_nodes()):
#    for j in range(G.number_of_nodes()):
#        if(partition[i]==partition[j]):
#            movie_modularity=partition[i].value();

    
print(partition.values().index(1))
print(movie_modularity)
