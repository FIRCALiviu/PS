import numpy as np
from ex4 import get_roots

X = np.linspace(0,10,1000)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(1000)

serie = trend+sezon+rezidual/100
serie = np.ones(1000) + rezidual/1000
p=7

def gen_serie_ar(y_serie,p):

    Y = np.zeros((len(y_serie)-p,p))

    for i in range(len(y_serie)-p):
        for j in range(p):
            Y[i][j] = y_serie[i+j]

    param = np.linalg.inv(Y.T@Y)@Y.T@y_serie[p:]

    return param
parametrii = gen_serie_ar(serie,p)
print('polinomul caracteristic: 1 +' ," + ".join([str(-i)+f'x^{k+1}' for k,i in enumerate(parametrii)]))
def get_coeff(parametrii):
    parametrii = -parametrii
    np.concat(([1],parametrii))
    a = parametrii[-1]
    parametrii /=a
    return parametrii[:-1]

carac = get_roots(get_coeff(parametrii))

carac = np.abs(carac)



v = carac[carac<1]

if len(v!=0):
    print('serie nestationara')