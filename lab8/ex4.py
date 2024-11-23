import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,1000,5000)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)


rezidual = np.random.randn(5000)

serie = trend+sezon+rezidual/100


train, test = serie[:int(len(sezon)*0.9)], sezon[int(len(sezon)*0.9):]

def built_Y(serie,p,m):
    Y = np.zeros((len(serie)-p-m,p))

    for i in range(len(serie)-p-m):
        for j in range(p):
            Y[i][j] = serie[i+j]
    return Y


def get_params(serie,p,m):
    Y = built_Y(serie,p,m)

    param = np.linalg.inv(Y.T@Y)@Y.T@serie[p+m:] # shiftam cu m imaginea din train data
    #, ca sa fie  orizontul mai departe cu m
    return param.T



for m in range(2,1000):
    t = float('inf')
    p_min = -1
    for p in range(2,13):
        pars  = get_params(train,p,m)
        
        pred = built_Y(test,p,m)@pars
        val = ((pred-test[p+m:])**2).sum()
        if t>= val:
            p_min = p
            t = val

    print('for m = {}, p optim = {}'.format(m,p_min))
    print(t)

# mi se pare aleatoriu dupa ce am facut domeniul mult mai mare, pentru ca este foarte precisa tehnica, orice p
# mai mare ca 3 e ok
