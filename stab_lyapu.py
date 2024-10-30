#Lyapunov Stability

import numpy as np 
import matplotlib.pyplot as plt 

#definimos el dominio D
x1=np.linspace(-3,3,100)
x2=np.linspace(-2,2,100)

#para poder usar la malla de D 
X1,X2=np.meshgrid(x1,x2)

V=lambda x1,x2: -x1**2 - x2**2 #la funcion definida 

fig, ax= plt.subplots(subplot_kw={"projection": "3d"}, figsize=(10,8))
surf=ax.plot_surface(X1,X2,V(X1,X2), cmap='viridis', linewidth=0,antialiased = False)
#para obtener las curvas de nivel 
ax. contourf(X1,X2, V(x1, X2), cmap='viridis',offset = -1)

#ahora definimos el cmapo vectorial 
u=-2*x1
v=-2*x2

#para graficarlo 
plt.quiver

