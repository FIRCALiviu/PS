import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,10)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(10)

serie = trend+sezon+rezidual/100


l = 5

lungime = len(X)

X = np.zeros((l,lungime-l+1))

for i in range(0,len(X[0])):
    for j in range(l):
        X[j,i] = serie[j+i]
