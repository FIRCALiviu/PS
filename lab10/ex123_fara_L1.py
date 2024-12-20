import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,1000)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(1000)

serie = trend+sezon+rezidual/100
p=12

def gen_serie_ar(y_serie,p):

    Y = np.zeros((len(y_serie)-p,p))

    for i in range(len(y_serie)-p):
        for j in range(p):
            Y[i][j] = y_serie[i+j]

    param = np.linalg.inv(Y.T@Y)@Y.T@y_serie[p:]




    pred = Y@(param.T)
    return pred

def gen_serie_ar_params_mascati(y_serie,params,p): # params  = 0 daca e mascat j si 1 daca nu
    Y = np.zeros((len(y_serie)-p,p))

    for i in range(len(y_serie)-p):
        for j in range(p):
            Y[i][j] = y_serie[i+j]*params[j]

    param = np.linalg.lstsq(Y,y_serie[p:])[0]




    pred = Y@(param.T)
    return pred
plt.plot(gen_serie_ar(serie,p))
plt.plot(serie[p:]) # seria creste repede deci ar este doar un offset cu seria
plt.show()

p=50 # acum o sa fie parametrii redundanti




list_params = []

def get_new_param(data,p, params): # params: solutia greedy pana acuma, nr natural returneaza parametrul in plus
    params_remaining = set((i for i in range(p))) - set(params)
    min_loss = float('inf')
    index_min = -1
    for i in params_remaining:
        params_ar = [0 ]*p
        params_ar[i] = 1
        for k in params:
            params_ar[k] = 1
        loss = ((gen_serie_ar_params_mascati(data,params_ar,p) - data[p:])**2).sum()
        print(loss)
        if loss < min_loss:
            min_loss = loss
            index_min = i
    return index_min

params_wanted = 9 # cat timp ruleaza greedy
params = []
for i in range(params_wanted):
    params.append(get_new_param(serie,p,params))
print(params) # rezultat : [45, 40, 35, 0, 10, 30, 15, 25, 47] in 30secunde