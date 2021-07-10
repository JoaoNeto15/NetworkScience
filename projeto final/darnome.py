import pandas as pd
import numpy as np
import csv

def mudar_rota1():
    df["Rota"]=1

def mudar_rota0():
    df["Rota"]=0

df = pd.read_csv("routes.csv")
print(df)
ar=[[]]
#df["Rota"]=5
df1 = pd.read_csv("Test.csv")
f = open('teste.csv','w',newline='')
x= []
writer = csv.writer(f)
reader = csv.reader("routes.csv")
for origem, destino in zip(df["Origem"],df["Destino"]): #ficheiro routes
    for o, d in zip(df1["orgiem"],df1["destino"]): #ficheiro rangel
    #print("O",origem, "D",destino)
        if origem == o and destino == d:
            x.append('1')
            writer.writerow(x)
            print(origem , "  ", destino)
        else:
            writer.writerow('0')
#print(df)
