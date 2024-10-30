import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 
plt.rcParams['text.usetex'] = True

# hacemos una funcion que tome los argumentos del pendulo para modelarlo 
def simple_pendulum(y, t, m, l, g, kf):
    x1, x2 = y   # hacemos que y tome los valores de x1 & x2 en una matriz 
    
    # sacamos la derivada de x1 que hicimos en clase el 12/8/24 
    dxdt = [x2,
            -g/l*np.sin(x1) - kf/m*x2]
    
    return dxdt

# system parametres 
m = 0.5 #mass
l = 0.30 # length of pendulum
kf = 0.1 # friction coefficient
g = 9.81 #gravity

# Initial conditions 
y0 = [np.pi/4, 0.0]

#simulation parametres //// time of simulation 
t = np.linspace(0, 15, 1000)

#solution of the system will be described by 
sol = odeint(simple_pendulum, y0, t, args=(m,l,g,kf))


#graficamos soluciones 
plt.plot(t, sol[:, 0], 'b', label = r'$x_1(t)$') # se grafica el pendulo simple en de posicion 0 de y es decir la posicion angular 
plt.plot(t, sol[:, 1], 'g', label = r'$x_2(t)$') # se grafica el pendulo simple en de posicion 1 de y es decir la aceleracion angular 
plt.legend(loc='best')
plt.xlabel('Time')
plt.grid()
plt.show()

# indicamos que x1 es la sol en 0 & 1 de nuestro vector y 
x1 = sol[:,0]
x2 = sol[:,1]

xpp = -g/l*np.sin(x1) - kf/m*x2 # posicion del pendulo

h = t[1] - t[0] # de acuerdo con el teorema de la derivada necesitamos un cambio o paso "h" que va a ser este 

# ahora buscamos la acceleracion numerica del pendulo differenciando dos veces nuestra posicion 
xpp_num =  np.diff(np.diff(x1)/h)/h
# si buscaramos su tamanio con xpp_num.shape veriamos que es dos valores mas pequenia que xpp porque perdemos valores al derivar numericamente 

# graficamos 
plt.figure
plt.plot(t, xpp)
plt.plot(t[:-2], xpp_num, '--') # ponemos el t[:-2] para tener ejes de las mismas dimensiones 
plt.show()


# ahora queremos saber que tan acertado es nuestro modelo con modelos de error de nuestro modulo benchmark 
#import benchmark
# no se porque no nos deja usar nuestro modul entonces lo escribimos aqui mismo 

def benchmark(y, yg):
    
    def mse(y, yg):
        return np.mean((y - yg)**2)
    
    def rmse(y, yg):
        return np.sqrt(mse(yg, y))
    #return np.sqrt (np.mean((y - yg)**2))
    
    def mae(y, yg):
        return np.mean(np.abs(yg - y))
    
    def mape(y, yg):
        #e = y - yg
        
        return 100*np.mean(np.abs(y - yg))
    
    def fit(y, yg): 
        return 100*(1-np.linalg.norm(y-yg)/np.linalg.norm(y - np.mean(y)))
    
    results = {
        'MSE': mse(y, yg),
        'RMSE': rmse(y, yg),
        'MAE': mae(y, yg),
        'MAPE': mape(y, yg),
        'FIT': fit(y, yg)
        }
    
    return results 

resultados = benchmark(xpp[:-2], xpp_num)
print(resultados)





#####################################################################
#### forma de modelar con euler a mano ####
## lo siguiente es ya con los parametros del sistema pero no con las condiciones iniciales 

# h = 1e-3
# Tfin = 20
# N = int((Tfin-h)/h)

# t = np.zeros(N)
# X1 = np.zeros(N)
# X2 = np.zeros(N)

# X1[0] = np.pi/4
# X2[0] = 0

# for k in range(N-1):
#     t[k+1] = t[k] + h
#     X1[k+1] = X1[k] + h*(X2[k])
#     X2[k+1] = X2[k] + h*(-(g/l)*np.sin(X1[k+1])-(kf/m)*X2[k])

# plt.figure
# plt.plot(t, X1)
# plt.show()
  
##############################################################################