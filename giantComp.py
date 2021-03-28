from networkx import nx
import sys
import random
from collections import defaultdict
f = open(sys.argv[1],'r')
n = f.readline()
s = ""
G = nx.Graph()
count = defaultdict(int)
for x in f.readlines():
    s = x.split(' ')
    G.add_edge(int(s[0]),int(s[1]))
component = max(nx.connected_components(G), key=len)
print("Size > component", len(component))
f.close()
