import numpy as np,matplotlib.pyplot as plt
x=np.array([10,5,20,15,8])
y=np.array([30500,58000,14900,20400,37000])
eq=np.polyfit(x,y,1)
plt.scatter(x,y,label="Data Points")
fun=np.poly1d(eq)
fir=fun(0)
sec=fun(20)
plt.plot([0,20],[fir,sec],label="Fitted Line")
plt.scatter([12],[fun(12)],c=[2],label="Estimate for 12th Year")
plt.legend()
plt.show()
print(fun(12))

