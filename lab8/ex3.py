import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,1000)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(1000)

serie = trend+sezon+rezidual/100

serie, test = serie[:int(len(serie)*0.9)], serie[int(len(serie)*0.9):]

p= 12

Y = np.zeros((len(serie)-p,p))

for i in range(len(serie)-p):
    for j in range(p):
        Y[i][j] = serie[i+j]

param = np.linalg.inv(Y.T@Y)@Y.T@serie[p:]
print(param)

Y_test = np.zeros((len(test)-p,p))

for i in range(len(test)-p):
    for j in range(p):
        Y_test[i][j] = test[i+j]


pred = Y_test@(param.T)


fig,(x,y) = plt.subplots(2)

x.plot(pred)
x.set_title("predictii")

y.plot(test[p:])
y.set_title("actual")

plt.savefig("ex3.png")
plt.show()