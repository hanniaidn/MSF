import control as ctrl
import matplotlib.pyplot as plt
import numpy as np 

# parámetros del sistema
Vin = 1
R = 1000
C = 1000e-6

#asi podemos definir las funciones de transferencia
num = 1/(R*C)
den = [1, 1/(R*C)]
sis1 = ctrl.tf(num, den)
t,y=ctrl.step_response(sis1) #step response le pone la U(s) a nuestra funcion 

#otra opcion 
s=ctrl.tf('s')
sis2=(1/(R*C))/(s+1/(R*C))

#funcion de tiempo, ya resuelta 
yt=lambda Vin, t, R, C : Vin*(1-np.exp(-t/(R*C))) 

plt.figure()
plt.plot(t,y) 
plt.plot(t,yt(Vin, t, R, C),'--')
plt.show()