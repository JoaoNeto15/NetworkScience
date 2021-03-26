import matplotlib.pyplot as plt
from networkx import nx
import sys
n = int(sys.argv[1])
p = float(sys.argv[2])
if(p == 0.005):
    f = open('random2.txt', 'w')
if(p==0.0001):
    f = open('random1.txt', 'w')
f.write(str(n)+'\n') #escreve n
G = nx.erdos_renyi_graph(n,p)
for e in list(G.edges()):
    f.write(str(e)+'\n') #escreves arestas no ficheiro
f.close()
nx.draw(G,node_color='#DAA520')
plt.show()