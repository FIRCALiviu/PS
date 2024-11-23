import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,100)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(100)

serie = trend+sezon+rezidual/100


# calculam autocorelatia

serie_teren = np.concat((np.zeros_like(serie),serie))

rez = []

for i in range(len(serie)):
    rez.append(np.sum(serie*serie_teren[i:(i+len(serie))]))

plt.xlabel("0 = delay maxim, final = suprapus")

plt.plot(rez)
plt.savefig("ex2.png")
plt.show()
"""
nu exista functie de autocorelatie in numpy

aceasta cantitate vrea sa masoara daca tipul de date are periodicitati 

"""
