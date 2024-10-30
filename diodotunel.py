import numpy as np 
import matplotlib.pyplot as plt 
import scipy
from scipy.integrate import odeint
 
#diodo tunel 
#primero resolvemos para h(x1)
x0 = -5
def h(x1):

    17.76*x1-103.79*x1**2+229.62*x1**3-226.31*x1**4+83.72*x1**5

print scipy.optimize.fsolve(h, x0)


