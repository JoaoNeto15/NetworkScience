import networkx as nx

from modularity_maximization import partition
from modularity_maximization.utils import get_modularity


G = nx.read_gml('bladerunner.gml')

#print(nx.info(G))

comm_dict = partition(G)

count = 0

for comm in set(comm_dict.values()):
    count+=1
    print("Community %d"%comm)
    print(', '.join([node for node in comm_dict if comm_dict[node] == comm]))

print("The total number of communities is: %d" % count)

print('Modularity is: %.3f' % get_modularity(G, comm_dict))