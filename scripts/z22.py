import numpy as np 
import scipy as sp
from scipy import interpolate
import matplotlib.pyplot as plt 
import pandas as pd
fig = plt.figure() 
ax = fig.add_subplot(111) 

file = pd.read_excel('../rec.xlsx')
y = file['U, В']
x = file['I,мА']
y = np.array(y[0:-1])
x = np.array(x[0:-1])
y_false = np.insert(y,9,224)
x_false = np.insert(x,9,0.032)
f = interpolate.interp1d(x_false,y_false,kind='quadratic')

x0 = np.linspace(min(x),max(x),10000)
ax.semilogx(x0,f(x0),color="darkblue",label='сплайн-интерполяция')
ax.semilogx(x,y,'ko', color = "brown", markersize=4,label='практика') 
plt.xlabel('$J$, мА') 
plt.ylabel('$U$,В') 
plt.grid(which='minor',linestyle=":") 
plt.grid(which='major',linestyle="-") 
plt.minorticks_on()
plt.legend()
plt.savefig('fig2.pdf', bbox_inches="tight")
plt.show()
