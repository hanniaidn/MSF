## levitador magnético ## 
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import control as ctrl

def magneticLevitator(y, t, m, g, R, c, L, u):
    x1, x2, x3 = y # hacemos que y tome los valores de x1 & x2 & x3 en una matriz 
    
    dxdt = [x2,
            g - ((c/m)*(x3**2/x1)),
            (-R/L)*x3 + ((u/L))]
    
    return dxdt

def spicySolution(y0, t, m, g, R, c, L, u):
    sol = odeint(magneticLevitator, y0, t, args = (m, g, R, c, L, u))
    
    x1 = sol[:, 0]
    x2 = sol[:, 1]
    x3 = sol[:, 2]

    xpp = g - (c/m)*(x3**2/x1) #velocidad del objeto
    
    h = t[1] - t[0] # de acuerdo con el teorema de la derivada necesitamos un cambio o paso "h" que va a ser este 
    
    xpp_num = np.diff(np.diff(x1)/h)/h
    
    return sol, xpp, xpp_num

def plotMultiple(t, y_data, labels = None, title = None, line_styles = None, xlabel = 'Tiempo (s)', ylabel = None):
    plt.figure()
    
    #si no se especifican estilos, usa una línea continua por defecto para todas
    if line_styles is None:
        line_styles = ['-'] * len(y_data)
    
    #graficar cada conjunto de datos con su correspondiente estilo de línea
    if labels is None:
        for y, style in zip(y_data, line_styles):
            plt.plot(t, y, style)
    else:
        for y, label, style in zip(y_data, labels, line_styles):
            plt.plot(t, y, style, label=label)
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.grid(True)
    
    #solo mostrar la leyenda si se proporcionaron etiquetas
    if labels:
        plt.legend()
    
    plt.show()

if __name__ == '__main__':
    
    # parámetros del sistema
    m = 0.05  # masa
    c = 0.0049 #capacitancia
    R  = 10 #resietancia
    L = 0.060 #inductancia
    u = 10 #netrada del sistema
    g = 9.81  # gravedad
    
    #simulación usando spicy
    y0 = [0.05, 0, 0]
    ts = np.linspace(0, 15, 1000)
    sol, xpp, xpp_num = spicySolution(y0, ts, m, g, R, c, L, u)
    
    y = [sol[:, 0], sol[:, 1], sol[:, 2]]
    label = [ r'$x_1(t)$', r'$x_2(t)$']
    plotMultiple(ts, y, label)
    
## sistema lineal ## 
x1=0.5
x2=0
x3=u/R
A = np.array([[0, 1, 0],
             [((-c/m)*(x3**2/x1**2)), 0, ((-2*c/m)*(x3/x1))],
             [0, 0, -R/L]])

B = np.array([[0],
              [0],
              [1/L]])

C = np.array([0.05, 0, 0])

mg_SL= ctrl.ss(A, B, C, 0)
print(mg_SL)
yout, T = ctrl.step_response(mg_SL)

plt.figure(2)
plt.plot(T.T, yout.T)
plt.show(block=False)