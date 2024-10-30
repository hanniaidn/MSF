import numpy as np 
import matplotlib.pyplot as plt

#para importar latex 
#plt.rcParams['text.usetex']=True

def benchmark(yg,y): #definimos funcion 
    def mse(yg,y): #definimos subfuncion
        return np.mean((yg-y)**2)
    
    def rmse(yg,y): #otra subfuncioncita
        return np.sqrt(mse(yg,y))
        #return np.sqrt(np.mean((yg-y)**2)) //tenemos dos opciones para poner el RMSE
        
    def mae(yg,y): 
        return np.mean(np.abs(yg-y))
    
    def mape(yg,y): 
        e=y-yg #definimos nuestra restita 
        return 100*np.mean(np.abs(e/y)) #easier 
    
    def fit(yg,y):
        return 100*(1-np.linalg.norm(y-yg)/np.linalg.norm(y-np.mean(y)))
    
    #ahora definimos un diccionario
    results = {
        'MSE':mse(yg,y),
        'RMSE':rmse(yg,y),
        'MAE':mae(yg,y),
        'MAPE':mape(yg,y),
        'FIT':fit(yg,y)
    }
    
    return results 

#para verificar su funcionamiento, creamos un vector artificial 
t=np.linspace(0,10,1000)
y=np.random.rand(1000)
yg=y+0.1*np.ones(1000)

resultados=benchmark(yg,yg)
print(resultados)

#ahora ploteamos 
plt.figure()
plt.plot(t,y,label='y(t)')
plt.plot(t,yg,label='yg(t)')
plt.xlabel('Time')
plt.legend(loc='best')
plt.show()
