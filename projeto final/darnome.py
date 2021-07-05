import pandas as pd
import numpy as np

from csv import writer
from csv import reader

def mudar_rota1():
    print("mudar 1")
    #writer.write(",1")

def mudar_rota0():
    print("mudar 0")
    #writer.write(",0")

df = pd.read_csv("routes.csv")
print(df)

#df["Rota"]=5

df1=pd.read_csv('Test.csv') 

#with open('Test.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
    


for origem, destino in zip(df["Origem"],df["Destino"]): #ficheiro routes
    '''
    for o, d in zip(df1["orgiem"],df1["destino"]): #ficheiro rangel
    #print("O",origem, "D",destino)
        if origem == o and destino == d:
            mudar_rota1()
            
            #acrescentar nessa linha um 1 na coluna rota
            #df['Rota'] = df['Rota'].replace({'3': '1'})
            print(origem , "  ", destino)
            print("UAU")
        #df['Rota'] = df['Rota'].replace({'3': '0'})
        #mudar_rota0()'''
    

    with open('Test.csv', 'r') as read_obj, \
        open('outputTest.csv', 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Append the default text in the row / list
            row.append(',0')
            # Add the updated row / list to the output file
            csv_writer.writerow(row)






print(df)
