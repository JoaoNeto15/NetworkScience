library(igraph)
library(readr)

# read bladerunner gml file
bladeRunner = read_graph("bladerunner.gml",format = "gml")

# read gephi files
edges = read_csv("edges_bladeRunner2.csv") 
nodes = read_csv("node_bladeRunner2.csv")


# bringing partition from gephi to R
V(bladeRunner)$color <- nodes$modularity_class+1
plot(bladeRunner, layout = layout_with_fr,
     edge.label = NA,
     vertex.label.cex =1, vertex.size = 20, vertex.color=V(bladeRunner)$color)




### calculate modularity
bladeRunner_AdjacencyMatrix = get.adjacency(bladeRunner, sparse=FALSE) # adjacency matrix
m = gsize(bladeRunner) # total number of edges 
bladeRunner_Communities <- nodes$modularity_class+1

bladeRunner_Modularity = 0

for(i in 1:vcount(bladeRunner)){
  for(j in 1:vcount(bladeRunner)){
    if(bladeRunner_Communities[i]==bladeRunner_Communities[j])
    bladeRunner_Modularity = bladeRunner_Modularity +
      bladeRunner_AdjacencyMatrix[i,j] -
      (degree(bladeRunner)[i]*degree(bladeRunner)[j])/(2*m)
  }
}
bladeRunner_Modularity = bladeRunner_Modularity/(2*m)


print(paste("Modularity of the bladeRunner grpah:",round(bladeRunner_Modularity,4)))

