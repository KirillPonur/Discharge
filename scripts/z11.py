import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
file = pd.read_excel('../rec.xlsx')
fig = plt.figure() 
ax = fig.add_subplot(111) 

x= file['l1,см']
y= file['U1,В']
ax.plot(x,y,'ko', color = "yellowgreen", markersize=4) 

x= file['l2, см']
y= file['U2, В']
ax.plot(x,y,'ko', color = "crimson", markersize=4)  


x= file['l3, см']
y= file['U3, В']
ax.plot(x,y,'ko', color = "indigo", markersize=4) 
ax.legend(('$I = 1.0015$ мА','$I = 2.0000$ мА','$I = 3.0000$ мА'))
plt.xlabel('$d_{\\text{ак}}$,см') 
plt.ylabel('$U_r$,В') 
plt.grid(which="major") 
plt.grid(which="minor",linestyle=":") 
plt.minorticks_on()
plt.savefig('fig1.pdf',bbox_inches="tight")
plt.show()
