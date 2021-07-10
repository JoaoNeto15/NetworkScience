
#CRIAR FICHEIRO COM INFO DE LATITUDE E LONGITUDE PARA A RANGEL + ROTAS
import csv
import pandas as pd
ficheiro = open('Porto.csv', 'r')
reader = csv.reader(ficheiro)

with open("info_porto.csv", 'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for linha in reader:
        #print (linha[1], linha[2])
        if(linha[2]==""):
            print("iu")
        s = linha[1]

        # with open("fligths_nodes.csv") as f_obj:
        #     reader = csv.reader(f_obj, delimiter=',')
        #     for line in reader:      #Iterates through the rows of your csv
        #         # line 6 : iata
        #         # line 8: latitude
        #         # line 9: longitude
        #         if line[6] == s:
        #             lista = []
        #             lista.append(s)
        #             lista.append(float(line[8]))
        #             lista.append(float(line[9]))
        #             for i in range(0,len(lista),3): # step by threes.
        #                 csvwriter.writerow(lista[i:i+3])
                    
        #             print(lista)
        #             break