import networkx as nx
import matplotlib as plt

#file="graph1.txt"
file="graph2.txt"

G = nx.read_edgelist(file,create_using=nx.Graph(), nodetype = int)

#Mount the graph with the properties
countA=0
countB=0
countU=0

for i in G.nodes():
    
    if (i%10==0) or  (i%10==1)or (i%10==2)or (i%10==3):
        G.add_node(i,vote="A")
        countA+=1
    elif (i%10==4) or  (i%10==5) or (i%10==6) or (i%10==7):
        G.add_node(i,vote="B")
        countB+=1
    else:
        G.add_node(i,vote="U")
        countU+=1



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


for x in range(11):


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

    #print("countAaux: ",countAaux)
    #print("countBaux: ",countBaux)
    #print("countUaux: ",countUaux)

    #iterações
    print("--------------------------------------------- x: ",x)

    hasU=True
    iteration=-1
    countU=-1

    for j in range(10*x):
        #print("j: ",j," A ")
        G.nodes[j+3000]['vote']="A"
    

    # Do the cicle while someone is still deciding how to vote
    while hasU:
        iteration+=1
        hasU=False
        countUanterior=countU
        countA=0
        countB=0
        countU=0
        list=[]

        # search for new voters
        for i in G.nodes():
            if (G.nodes[i]['vote']=="U"):
                hasU=True
                countU+=1
                list.append((i,vote(i)))
                #G.nodes[i]['vote']=vote(i)
            elif G.nodes[i]['vote']=="A":
                countA+=1
            elif G.nodes[i]['vote']=="B":
                countB+=1

        # show results
        #print("iteração: ",iteration)
        #print("countA: ",countA)
        #print("countB: ",countB)
        #print("countU: ",countU)
        #print("Diff: ",countB-countA)

        #Changing the votes that had decided in this round
        for i in list:
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