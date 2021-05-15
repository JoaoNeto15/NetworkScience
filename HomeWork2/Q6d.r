library(igraph)
library(readr)
library(RColorBrewer)

# read bladerunner gml file
bladeRunner = read_graph("bladerunner.gml",format = "gml")

# read gephi files
edges = read_csv("edges_bladeRunner2.csv") 
nodes = read_csv("node_bladeRunner2.csv")


# finction to find calculate modularity and display plot
modularityFinder <- function(bladeRunner,bladeRunner_Communities){
  bladeRunner_AdjacencyMatrix = get.adjacency(bladeRunner, sparse=FALSE) # adjacency matrix
  m = gsize(bladeRunner) # total number of edges 
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
  V(bladeRunner)$color <- bladeRunner_Communities
  plot(bladeRunner, layout = layout_with_fr,
       edge.label = NA,
       vertex.label.cex =1, vertex.size = 20)
  # print(paste("Modularity of the bladeRunner grpah:",round(bladeRunner_Modularity,4)))
  return(round(bladeRunner_Modularity,4))
}

bladeRunner_Communities <- 1:vcount(bladeRunner)
# bladeRunner_Communities <- nodes$modularity_class+1
modularityFinder(bladeRunner,bladeRunner_Communities)


keepModularity = vector()
baseModularity = modularityFinder(bladeRunner,bladeRunner_Communities)
size = 0
vec = bladeRunner_Communities
for(i in 1:length(vec)){
  for( j in i+1:length(vec)){
    if( j<=length(vec)) {
      testPartition = replace(vec,i,j)
      currentModularity =  modularityFinder(bladeRunner,testPartition)
      if(currentModularity>baseModularity){
        largePartion = testPartition
        largeModularity = currentModularity
      }
    }
  }
  print(largeModularity)
  keepModularity[length(keepModularity)+1] = largeModularity
  baseModularity = largeModularity
  print(largePartion)
  vec = largePartion
}


plot(keepModularity)

# Q6e: for getting more communities aim for lowest modularity (anti community structure)