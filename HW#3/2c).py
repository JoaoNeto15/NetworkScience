from typing import Sized
import networkx as nx
import matplotlib as plt

file="graph1.txt"
#file="graph2.txt"

G = nx.read_edgelist(file,create_using=nx.Graph(), nodetype = int)

#Mount the graph with the properties
countA=0
countB=0
countU=0
list=[]


for i in G.nodes():
    
    if (i%10==0) or  (i%10==1)or (i%10==2)or (i%10==3):
        G.add_node(i,vote="A",degree=G.neighbors(i)) # procurar como se faz size
        list.append((i,)) # terminar
        countA+=1
    elif (i%10==4) or  (i%10==5) or (i%10==6) or (i%10==7):
        G.add_node(i,vote="B",degree=G.neighbors(i))
        countB+=1
    else:
        G.add_node(i,vote="U",degree=G.neighbors(i))
        countU+=1

