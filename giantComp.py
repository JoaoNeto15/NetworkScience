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
    s = x.split(',')
    s[0] = s[0].replace("(", "")
    s[1] = s[1].replace(")","")
    a = int(s[0])
    b = int(s[1])
    G.add_edge(a,b)
component = max(nx.connected_components(G), key=len)
print("Size > component", len(component))
f.close()
