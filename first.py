import numpy as np, matplotlib.pyplot as pl
x=[]
for i in range(-250,251):
    x.append((i/250)*np.pi)
func=np.polyfit(x,[28*np.sin(i) for i in x],4)
z=np.poly1d(func)
for i in range(len(func)):
    print("X",(len(func)-1-i),"=",func[i])
pl.plot(x,[28*np.sin(i) for i in x],label="Sin")
pl.plot(x,[z(i) for i in x],label="Fitted")
pl.legend()
pl.show()



