
#CRIAR FICHEIRO COM INFO DE LATITUDE E LONGITUDE PARA A RANGEL
import csv
import pandas as pd

ficheiro = open('NosEmFalta.csv', 'r')
reader = csv.reader(ficheiro)
s=""

with open("info_paisesBK.csv", 'w',newline='',encoding = 'utf8') as csvfile:
    #legenda = ["IATA", "LAT", "LONG"]
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerow(legenda)
    for linha in reader:
        #print linha[1]
        s = linha[0]
        print(s)

        with open("fligths_nodes.csv",'r', errors='ignore') as f_obj:
            reader2 = csv.reader(f_obj)
            
            for line in reader2:      #Iterates through the rows of your csv
                # line 6 : iata
                # line 8: latitude
                # line 9: longitude
                #linha 5: country
                if line[6] == s:
                    lista = []
                    # lista.append(s)
                    # lista.append(float(line[8]))
                    # lista.append(float(line[9]))
                    #lista.append(line[5])
                    lista.append(line)
                    #for i in range(0,len(lista),4): # step by threes.
                    print(line)
                    l=""
                    for i in line:
                        print("i: "+i)
                        l=l+i
                    #print(l)
                    csvwriter.writerow(line) 
                    break
                