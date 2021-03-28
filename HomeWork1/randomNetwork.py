import matplotlib.pyplot as plt
from networkx import nx
import sys
import re
n = int(sys.argv[1])
p = float(sys.argv[2])
s = ""
if(p == 0.005):
    f = open('random2.txt', 'w')
if(p==0.0001):
    f = open('random1.txt', 'w')
f.write(str(n)+'\n') #escreve n
G = nx.erdos_renyi_graph(n,p)
for e in list(G.edges()):
    s = str(e).split(',')
    s[0] = s[0].replace("(", "")
    s[1] = s[1].replace(")","")
    f.write(s[0])
    f.write(s[1])
    f.write('\n')
f.close()
nx.draw(G,node_color='#DAA520')
plt.show()