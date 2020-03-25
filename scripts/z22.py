import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
fig = plt.figure() 
ax = fig.add_subplot(111) 

file = pd.read_excel('../rec.xlsx')
y = file['U, В']
x = file['I,мА']
# x=np.array([0,0.2,0.26,0.3,0.34,0.36,0.38,0.4,0.44]) 
# y=np.array([0,1,8,14,28,38,54,74,100]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='blue', lw=0.5, mfc='white', ms=3) 


# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='black', lw=0.5, mfc='white', ms=3) 

# x=np.array([0,19.8,20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27]) 
# y=np.array([0,0.008,0.015,0.022,0.033,0.059,0.071,0.092,0.13,0.17,0.227,0.301,0.375,0.455,0.62,0.74,0.985]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='red', lw=0.5, mfc='white', ms=3) 


ax.semilogx(x,y,'ko', color = "brown", markersize=4) 
plt.xlabel('$J$, мА') 
plt.ylabel('$U$,В') 
plt.grid(which='minor',linestyle=":") 
plt.grid(which='major',linestyle="-") 
plt.minorticks_on()
plt.savefig('fig2.pdf', bbox_inches="tight")
plt.show()
