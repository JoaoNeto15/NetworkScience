import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
G = nx.DiGraph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(2, 4)
G.add_edge(4, 2)
G.add_edge(5, 4)
G.add_edge(2, 6)
G.add_edge(6, 5)
G.add_edge(6, 7)
G.add_edge(7, 6)
G.add_edge(2, 5)
n = G.number_of_nodes()
nodes = list(G.nodes)
#print(nodes[6])
######LISTA DE NÓS + IN-LINKS +OUT-LINKS#########
"""for i in range (1,8): 
    ind = G.in_degree(i)
    out = G.out_degree(i)
    print("NÓ", i, " IN-LINK" , ind , " OUT-LINK", out)"""
rank_atual={}
for j in range(1,8): #inicializar valor pagerank com 1/7 (normalizar)
    rank_atual[j] = 1/n

eps = 0.000001
x = 1.0
it = 0
beta = 0.85
rank_novo = rank_atual
while(x > eps):
    print("x", x, "eps ", eps)
    for no in G.nodes:
        adj = set(G[no]) #lista vizinhos
        #print("nó : ", no , " ", adj)
        for adj_i in adj:
            #print("in ", G.in_degree(adj_i))
            #print("NO", no)
            rank_novo[no] += (1-beta)/7 +(beta*(rank_atual[adj_i]/G.out_degree(adj_i))) #ri/di

            x = abs(rank_novo[no]-rank_atual[no])
            rank_novo = rank_atual
            it = it + 1
            print("iteração:", it)
            print()
            print("pagerank", rank_novo)
#nx.draw(G,node_color='#DAA520')
#plt.show()