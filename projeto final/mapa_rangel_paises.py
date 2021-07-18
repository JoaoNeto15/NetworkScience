
#CRIAR FICHEIRO COM INFO DE LATITUDE E LONGITUDE PARA A RANGEL
import csv
import pandas as pd

ficheiro = open('Porto_Lisboa.csv', 'r')
reader = csv.reader(ficheiro)

with open("info_paises.csv", 'w',newline='') as csvfile:
    #legenda = ["IATA", "LAT", "LONG"]
    csvwriter = csv.writer(csvfile, delimiter=',')
    #csvwriter.writerow(legenda)
    for linha in reader:
        #print linha[1]
        s = linha[1]

        with open("fligths_nodes.csv") as f_obj:
            reader = csv.reader(f_obj, delimiter=',')
            for line in reader:      #Iterates through the rows of your csv
                # line 6 : iata
                # line 8: latitude
                # line 9: longitude
                #linha 5: country
                if line[6] == s:
                    lista = []
                    # lista.append(s)

                    lista.append(line[3])
                    lista.append(line[4])
                    lista.append(line[5])
                    lista.append(line[6])
                    lista.append(float(line[8]))
                    lista.append(float(line[9]))
                    lista.append(line[10])
                    lista.append(line[11])
                    lista.append(line[12])
                    lista.append(line[13])
                    #for i in range(0,len(lista),4): # step by threes.
                    csvwriter.writerow(lista)
                    break
                    #for i in range(0,len(lista),4): # step by threes.
                        #csvwriter.writerow(lista[i:i+4])