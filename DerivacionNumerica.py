import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 1000) # x
h = x[1] - x[0] #delta_x

#lamda es una función respecto a una variable, en este caso x
f = lambda x: 3*x**2 + 3*x
fp = lambda x: 6*x + 3*np.ones(len(x))

#derivación numérica
N = len(x)
xd = np.zeros(N-1)

fx = f(x)


for k in range(N-1):
    #xd[k] = (f(x[k]+h) - f(x[k]))/h # si conozco el cuerpo de la función
    xd[k] = (fx[k+1] - fx[k])/h

plt.figure
plt.plot(x, fp(x))
plt.plot(x[:-1], xd,'-.')
plt.show()

e = fp(x[:-1]) - xd

plt.figure
plt.plot(x[:-1], e)
plt.show()