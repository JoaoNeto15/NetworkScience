from pylab import *
import networkx as nx
#importing pandas as pd
import pandas as pd
  
# Read and store content
# of an excel file 
read_file = pd.read_excel ("Air.xls")
  
# Write the dataframe object
# into csv file
read_file.to_csv ("Test.csv", 
                  index = None,
                  header=True)
    
# read csv file and convert 
# into a dataframe object
df = pd.DataFrame(pd.read_csv("Test.csv"))
  
# show the dataframe
df
print("D", df["destino"])
print("O", df["orgiem"])

import pandas
df = pandas.DataFrame(data={"origem": df["orgiem"], "destino": df["destino"], "peso": df["peso"]})
df.to_csv("./file.csv", sep=',',index=False)

#nx.draw(g)
#show()
