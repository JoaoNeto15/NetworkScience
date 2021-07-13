import pandas as pd
import numpy as np




#rangel = pd.read_csv("C:\Users\Carlos Neto\Documents\GitHub\NetworkScience\projeto final\AirCSVlis.csv")


#print(rangel)


import csv
with open('AirCSVlis.csv', 'w', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

#for origem, destino in zip(rangel["source"],rangel["target"]):
#    print("origem: ",origem,"  destino: ",destino)