import numpy as np
import matplotlib.pyplot as plt

m = 0.5
l = 0.30
kf = 0.0
g = 9.81

h = 1e-3
Tfin = 20
N = int((Tfin-h)/h)

x = np.linspace(-2,2,1000)
t = np.zeros(N)
X1 = np.zeros(N)
X2 = np.zeros(N)

X1[0] = np.pi/4
X2[0] = 0
xd = np.zeros(N-1)

for k in range(N-1):
    t[k+1] = t[k] + h
    X1[k+1] = X1[k] + h*(X2[k])
    X2[k+1] = X2[k] + h*(-(g/l)*np.sin(X1[k+1])-(kf/m)*X2[k])
    
#tarea moral 
#derivar numericamente x1 para obtener la aceleracion angular 
for k in range (N-1):
    xd[k] = (X1[k+1] - X2[k])/h
    
#calculamos MSE de ambas soluciones 
MSE = np.square(np.subtract(xd,X1[:-1])).mean()


plt.figure
plt.plot(t, X1)
plt.show()