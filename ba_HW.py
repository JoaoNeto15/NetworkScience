# BA MODEL IN PYTHON
# This Code is inspired and some functions to plot are from the folowing source:
#https://github.com/AlxndrMlk/Barabasi-Albert_Network

import networkx as nx
import numpy as np
import random as rd
import matplotlib.pyplot as plt
COLOR = '#40a6d1'

# Plotting
def k_distrib(graph, scale='lin', colour='#40a6d1', alpha=.8, fit_line=False, expct_lo=1, expct_hi=10, expct_const=1):
    
    plt.close()
    num_nodes = graph.number_of_nodes()
    max_degree = 0
    
    # Calculate the maximum degree to know the range of x-axis
    for n in graph.nodes():
        if graph.degree(n) > max_degree:
            max_degree = graph.degree(n)
    
    # X-axis and y-axis values
    x = []
    y_tmp = []
    
    # Loop over all degrees until the maximum to compute the portion of nodes for that degree
    for i in range(max_degree + 1):
        x.append(i)
        y_tmp.append(0)
        for n in graph.nodes():
            if graph.degree(n) == i:
                y_tmp[i] += 1
        y = [i / num_nodes for i in y_tmp] 
    
    # Check for the lin / log parameter and set axes scale
    if scale == 'log':
        plt.xscale('log')
        plt.yscale('log')
        plt.title('Degree distribution (log-log scale)')
        plt.ylabel('log(P(k))')
        plt.xlabel('log(k)')
        plt.plot(x, y, linewidth = 0, marker = 'o', markersize = 8, color = colour, alpha = alpha)
        
        if fit_line:
            # Add theoretical distribution line k^-3
            # Note that you need to parametrize it manually
            w = [a for a in range(expct_lo,expct_hi)]
            z = []
            for i in w:
                x = (i**-3) * expct_const # set line's length and fit intercept
                z.append(x)

            plt.plot(w, z, 'k-', color='#7f7f7f')
            
    else:
        plt.plot(x, y, linewidth = 0, marker = 'o', markersize = 8, color = colour, alpha = alpha)
        plt.title('Degree distribution (linear scale)')
        plt.ylabel('P(k)')
        plt.xlabel('k')

    plt.show()


# BA algo functions
def rand_prob_node():
    nodes_probs = []
    for node in G.nodes():
        node_degr = G.degree(node)
        node_proba = node_degr / (2 * len(G.edges()))
        nodes_probs.append(node_proba)
    random_proba_node = np.random.choice(G.nodes(),p=nodes_probs)
    return random_proba_node

def add_edge():
        if len(G.edges()) == 0:
            random_proba_node = 0
        else:
            random_proba_node = rand_prob_node()
        new_edge = (random_proba_node, new_node)
        if new_edge in G.edges():
            add_edge()
        else:
            G.add_edge(new_node, random_proba_node)
            #print("Edge added: {} {}".format(new_node + 1, random_proba_node))
            file.write("{} {}\n".format(new_node + 1, random_proba_node))



#Parameters 1
#init_nodes = 3
#final_nodes = 2000
#m_parameter = 1

#Parameters 2
#init_nodes = 5
#final_nodes = 2000
#m_parameter = 2

#arameters Teste
init_nodes = 12
final_nodes = 250
m_parameter = 7


file = open('ba1.txt', 'w')
file.write("{}\n".format(final_nodes))

# Creating initial graph

G = nx.complete_graph(init_nodes)

#Print the existing nodes (to_do)
#for i in range(G.)

count = 0
new_node = init_nodes

for f in range(final_nodes - init_nodes):
    G.add_node(init_nodes + count)
    count += 1
    for e in range(0, m_parameter):
        add_edge()
    new_node += 1

#Present the Distribution
k_distrib(G), k_distrib(G, scale = 'log', fit_line = False)

# Plot the network
nx.draw(G, alpha = 0.3, edge_color = COLOR, node_color = COLOR, node_size=50)
plt.show()
