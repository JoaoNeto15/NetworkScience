import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.CompositeModel as gc
import ndlib.models.compartments.NodeStochastic as ns

file="graph1.txt"
#file="graph2.txt"


g = nx.read_edgelist(file,create_using=nx.DiGraph(), nodetype = int)


print(nx.info(g))

# Composite Model instantiation
model = gc.CompositeModel(g)

# Model statuses
model.add_status("A")
model.add_status("B")
model.add_status("U")

# Compartment definition
c1 = ns(0.4, triggering_status="A")
c2 = ns(0.4, triggering_status="B") 

# Rule definition
model.add_rule("U", "A", c1)
model.add_rule("U", "B", c2)

# Model initial status configuration
config = mc.Configuration()
config.add_model_parameter('Votacao', 0.4)

# Simulation execution
model.set_initial_status(config)
iterations = model.iteration_bunch(5)




print(g)



# Está tudo mal fazer de novo mas de origem 