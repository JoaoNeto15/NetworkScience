import numpy as np; 
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [-0.5,0,0.5]
#plt.plot(k,x,marker="*", color='navy', label="circuit1")

plt.plot([0.94690,0.17789,0.13450,0.23154],marker="*", color='navy', label="circuit1")
plt.plot([0.95005,0.09013,0.07355,-0.28957],marker=".", color='mediumpurple', label="circuit2")
plt.plot([0.83447,0.15621,-0.34153,-0.40323],marker="v", color='turquoise', label="ecoli")
plt.plot([0.45528,0.38488,0.38131,0.33242,0.28773,-0.18308,-0.27526,-0.31345,-0.31358],marker="1", color='gold', label="english")
plt.plot([0.27889,0.25506,0.23266,0.16132,0.05179,-0.10876,-0,13815,-0.22878,-0.28601,0.30763,-0.32420,-0.53163],marker="P", color='green', label="french")
plt.plot([0.96491,0.19393,0.08318,0.06226,0.054149,0.02329,0.01763,0.01271,-0.02236,-0.2635,-0.06722,-0.07005,-0.7896],marker="x", color='tomato', label="highschool")
plt.plot([0.97296,0.16328,0.12887,0.03171,0.01805,0.01795,0.01585,0.00298,-0.01959,-0.02459,-0.04514,-0.05042,-0.05089],marker="d", color='olive', label="residende")
plt.plot([0.51098,0.13843,-0.45721,-0.47076,-0.53765],marker="+", color='purple', label="teal")
plt.plot([0.02171,0.01997,0.01955,0.01870,0.01652,-0.01042,-0.01584,-0.01742,-0.02028,-0.02296,-0.02342,-0.03275],marker="p", color='grey', label="spanish")
plt.xticks(x)
plt.yticks(y)
plt.ylim(0.5,-0.5)
plt.legend()
plt.show()