# Homework#3 2 a)

import networkx as nx
import matplotlib as plt

file="graph1.txt"
#file="graph2.txt"


G = nx.read_edgelist(file,create_using=nx.DiGraph(), nodetype = int)


print(nx.info(G))

#def voto:    função que calcula o seu voto


#iterar para todos
#if (mod(8,9) (ver vizinhos))


# fazer para todos os nós
