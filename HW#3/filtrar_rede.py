import csv
import pandas as pd
from os import lstat
def create_network_from_ﬁle(file):
    f = open(file)
    aux = csv.reader(f, delimiter='\t')
    count=0
    count_a=0
    count_b=0
    lista=[]
    df = pd.read_csv('raw_unicode.csv', index_col=0)
    for linha in aux:
        s = linha[0].split(',')
        pais = s[0]
        id_pais = s[1]
        linguagem=s[2]
        id_linguagem=s[3]
        populacao = s[4]
        percentagempop = s[5]
        count = count + 1
        #print(pais ," ", id_pais, " ", linguagem, " ", id_linguagem, " ", populacao, " ", percentagempop)
        if(not(float(percentagempop) < 0.10 and float(populacao) < 10000000)):
            print(percentagempop)
            lista.append(linha)
            count_a = count_a +1
        #remover linguagens que são faladas por menos de 10M pessoas
        """if(float(populacao) < 10000000):
            lista.append(linha)
            print(linguagem)
            count_b = count_b+1"""
    criar(lista)
    print(count)

def criar(lista):
    f = open('teste.csv','w',newline='')
    writer = csv.writer(f)
    count=0
    for x in lista:
        writer.writerow(x)
        count = count +1
    f.close()
    print("j",count)
create_network_from_ﬁle('raw_unicode.csv')
