from typing import Sized
import networkx as nx
import matplotlib as plt

#file="graph1.txt"
file="graph2.txt"

G = nx.read_edgelist(file,create_using=nx.Graph(), nodetype = int)

#Mount the graph with the properties
countA=0
countB=0
countU=0
list=[] # (no,grau)



for i in G.nodes():
    
    if (i%10==0) or  (i%10==1)or (i%10==2)or (i%10==3):
        G.add_node(i,vote="A",degree=G.degree(i)) # procurar como se faz size
        list.append((i,G.degree(i))) # terminar
        countA+=1
    elif (i%10==4) or  (i%10==5) or (i%10==6) or (i%10==7):
        G.add_node(i,vote="B",degree=G.neighbors(i))
        list.append((i,G.degree(i)))
        countB+=1
    else:
        G.add_node(i,vote="U",degree=G.neighbors(i))
        list.append((i,G.degree(i)))
        countU+=1

# ordenação
list.sort(reverse=True,key=lambda a: (a[1],-a[0]))

list2=list[:21]
print(list2)


# Function that decide to vote 
def vote(n):
    voteN="U"
    countAf=0
    countBf=0

    for i in G.neighbors(n):
        if G.nodes[i]['vote']=="A":
            countAf+=1
        elif G.nodes[i]['vote']=="B":
            countBf+=1
    
    if countAf>countBf:
        voteN="A"
    elif countBf>countAf:
        voteN="B"

    return voteN


for x in range(len(list2)):
    # Reset ao grafo
    countAaux=0
    countBaux=0
    countUaux=0

    for n in G.nodes():
        if (n%10==0) or  (n%10==1)or (n%10==2)or (n%10==3):
            G.nodes[n]['vote']="A"
            countAaux+=1
        elif (n%10==4) or  (n%10==5) or (n%10==6) or (n%10==7):
            G.nodes[n]['vote']="B"
            countBaux+=1
        else:
            G.nodes[n]['vote']="U"
            countUaux+=1

    #iterações
    print("--------------------------------------------- x: ",x)

    hasU=True
    iteration=-1
    countU=-1

    print("list2[0]: ",list2[x])


    for j in range(x):
        G.nodes[list2[j][0]]['vote']="A"


    # Do the cicle while someone is still deciding how to vote
    while hasU:
        iteration+=1
        hasU=False
        countUanterior=countU
        countA=0
        countB=0
        countU=0
        list3=[]

        # search for new voters
        for i in G.nodes():
            if (G.nodes[i]['vote']=="U"):
                hasU=True
                countU+=1
                list3.append((i,vote(i)))
                #G.nodes[i]['vote']=vote(i)
            elif G.nodes[i]['vote']=="A":
                countA+=1
            elif G.nodes[i]['vote']=="B":
                countB+=1


        #Changing the votes that had decided in this round
        for i in list3:
            G.nodes[i[0]]['vote']=i[1]
        
        #if no one else whant to vote
        if countU==countUanterior:
            break 

    # show results
    print("iteração: ",iteration)
    print("countA: ",countA)
    print("countB: ",countB)
    print("countU: ",countU)
    print("Diff: ",countB-countA)

