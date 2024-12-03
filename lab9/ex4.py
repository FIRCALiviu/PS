import numpy as np
import matplotlib.pyplot as plt
q=4
p= 12
X = np.linspace(0,10,1000)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(1000)

serie = trend+sezon+rezidual
medie_save=serie.mean()
serie -=serie.mean()


medie = serie.mean()
erori = np.zeros(q)
coeff = np.ones(q) /q


y_pred = serie[q:]

def get_serie(coeff,serie):
    serie_noua = []
    for i in range(q,len(serie)):
        predict = -np.dot(erori,coeff) 
        serie_noua.append(predict)
        erori[0:q-1] = erori[1:q]
        erori[q-1] = predict-serie[i]
    return serie_noua


def get_error(plot=False):

    Y = np.zeros((len(serie)-p,p))

    for i in range(len(serie)-p):
        for j in range(p):
            Y[i][j] = serie[i+j]

    param = np.linalg.inv(Y.T@Y)@Y.T@serie[p:]
    


    pred = Y@(param.T)

    goal = serie.copy()[p:]

    goal-=pred # serie = ar+ma => ma = serie-ar ca sa simplifice calculul


    goal2=get_serie(coeff,goal)

    rez = pred[q:]+goal2
    if plot:
        plt.plot(rez,label="predictii")
        plt.plot(serie,label='serie')
        
        plt.legend()
        
        plt.savefig("ex4.png")
        plt.title(f"predicii vs serie")
        plt.show()
    return np.sum((rez-serie[q+p:])**2)

m = float('inf')

index = -1

for i in range(2,10):
    for j in range(2,10):
        
        p=i
        q=j
        erori = np.zeros(q)
        coeff = np.ones(q) /q
        error = get_error()

        if error<m:
            m=error
            index = [i,j]
        print(f"pentru p={i} si q={j} ,eroare {error}")

print(f"minim optim: {m} cu valori p:{index[0]} q:{index[1]}")

get_error(True)