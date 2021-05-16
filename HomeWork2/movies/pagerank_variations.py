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
rank_atual={}
for j in range(1,8): #inicializar valor pagerank com 1/7 (normalizar)
    rank_atual[j] = 1/n

eps = 0.000001
x = 1.0

beta = 0
count_it =0
b_i=[] #para valores de beta
y_i=[] #valores de it
p_i=[] #valores page_rank
it = 0


rank_novo = rank_atual
while(beta <= 1):
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
            for i in rank_novo:
                print(rank_novo[i])
                p_i.append(rank_novo[i])
    it = it+1
    beta = beta + 0.005
    b_i.append(beta)
    y_i.append(it)
plt.plot(b_i,y_i,color='#DAA520') #beta /valores a)
#plt.plot(p_i,color='#DAA520') #valores b)
plt.show()
#nx.draw(G,node_color='#DAA520')
#plt.show()