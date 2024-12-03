import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0,10,1000)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(1000)

serie = trend+sezon+rezidual

q=4

serie-=serie.mean()
erori = np.zeros(q)
coeff = np.ones(q) /q


y_pred = serie[q:]

def get_serie(coeff):
    serie_noua = []
    for i in range(q,len(serie)):
        predict = -np.dot(erori,coeff) 
        serie_noua.append(predict)
        erori[0:q-1] = erori[1:q]
        erori[q-1] = predict-serie[i]
    return serie_noua



plt.plot(get_serie(coeff))
plt.plot(serie)
plt.savefig('ex3.png')
plt.show()
