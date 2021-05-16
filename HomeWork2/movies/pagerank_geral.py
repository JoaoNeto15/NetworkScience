import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
G = nx.DiGraph()
n = G.number_of_nodes()
nodes = list(G.nodes)
rank_atual={}
for j in range(1,8): #inicializar valor pagerank com 1/7 (normalizar)
    rank_atual[j] = 1/n

eps = 0.00001
x = 1.0
it = 0
beta = 0.85
rank_novo = []
while(x > eps):
    for no in G.nodes:
        adj = set(G[no]) #lista vizinhos
        #print("nó : ", no , " ", adj)
        for adj_i in adj:
            #print("in ", G.in_degree(adj_i))
            #print("NO", no)
            rank_atual[no] += (1-beta)/7 +(beta*(rank_atual[adj_i]/G.out_degree(adj_i))) #ri/di
            rank_novo = rank_atual
        x = abs(rank_novo[no]-rank_atual[no])

        it = it + 1
        print("iteração:", it, "pagerank", rank_novo)