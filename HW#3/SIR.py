#numero simulações k = 3
#dias =100
#beta = 4%
#delta = 1/4
import numpy as np
import matplotlib.pyplot as plt
n = 10000
t = 100 #dias
i = 5 # infetados
r = 0 #recuperados
s = 9995 #suscetiveis
infetados =[]
suscetievis=[]
recuperados =[]
beta = 0.04
#beta  = 0.01
delta = 1/14
gama = 7 #imunidade c/ vacina
print("Ro", beta/delta)
suscetievis.append(s)
infetados.append(i)
recuperados.append(r+gama)
print("s",s, " i", i, " r", r)
for k in range(1,100):
    dS = -beta*s*(i/t)
    dI = beta*s*(i/t) -t -delta*(i)
    dR = delta * (i) 
    s =  abs(dS)
    suscetievis.append(int(s))
    i = abs(dI) - i 
    infetados.append(int(i))
    r = abs(dR) + gama
    recuperados.append(int(r))
    print("s: ", int(s), "i: ", int(i), "r: ",int(r), "iteração ", k)

    #R0 
Ro = beta/delta
print("ro",Ro)
#MÉDIAS DE CASOS
m_s =sum(suscetievis)/len(suscetievis)
m_i =sum(infetados)/len(infetados)
m_r =sum(recuperados)/len(recuperados)
print("média suscetiveis ", int(m_s), "media infetados ", int(m_i), "media recuperados", int(m_r))


#PICO DE INFETADOS

max = 0
max_i = 0
for i, valor in enumerate(infetados):
    if (max is None or int(valor) > max):
        max = int(valor)
        max_i = i

print("valor máximo ", max, "dia: ", max_i)


#plt.plot(suscetievis,color='navy', label="suscetiveis")
plt.plot(infetados, color='green', label="infetados")
plt.plot(recuperados,color='red', label="recuperados")

plt.xlabel("Tempo/dias")
#plt.xlim([0,15])
#plt.ylim([0,10000])
plt.ylabel("Casos")
plt.legend()
#plt.yticks(np.arange(0, 100, 1.0))
plt.show()