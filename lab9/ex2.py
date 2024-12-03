import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,100)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(100)

serie = trend+sezon+rezidual

serie = np.array([1,2,3,4,5])

def s(a,vec):
    rez = [vec[0]]
   
    for i in range(1,len(vec)):
        rez.append(a*vec[i]+(1-a)*rez[i-1])
       
    
    return np.array(rez)

def get_error(a,vec):
    
    preds = s(a,vec[:-1])
    
    return np.sum((preds-vec[1:])**2)

optim_min = float('inf')
index_optim = -1
for i in np.linspace(0,1,500):
    if ( Error:=get_error(i,serie) ) < optim_min:
        optim_min = Error
        index_optim = i
        print(optim_min,index_optim)


print(index_optim)
plt.plot(serie[1:],label = 'seria timp')
plt.plot(s(index_optim,serie[:-1]),label='preds')
plt.legend()
plt.show()

