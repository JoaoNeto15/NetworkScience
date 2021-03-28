import matplotlib.pyplot as plt
from networkx import nx
from itertools import combinations
import sys
import random
n = int(sys.argv[1])
p = 0.0001
plt.ylabel('tamanho componente')
plt.xlabel('p')
x=[]
y=[]
while p <= 0.005:
    x.append(p)
    G = nx.erdos_renyi_graph(n,p)
    for u, v in combinations(G, 2):
        if random.random() < p:
            G.add_edge(u, v)
    component = max(nx.connected_components(G), key=len)
    y.append(len(component))
    p = p + 0.0001
plt.plot(x, y, marker='o', linestyle='--', color='#DAA520', label='Square')
plt.show()