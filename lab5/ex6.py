import numpy as np

import matplotlib.pyplot as plt

import csv

file = open("Train.csv")

vec = list(csv.reader(file))

data = np.array(vec[1:])[:,2].astype(np.float32)

data -= data.mean()




procesare = np.abs(np.fft.fft(data))

N = 18288



plt.plot((1/3600)*np.arange(0,N//2,1)/N,procesare[:N//2])
plt.xlabel('frecventa Hz')
plt.show()

# ne concentram doar pe argumentele pozitive
data = procesare[:N//2]
top4 = np.argsort(data)[-4:]

def f_a(m):
    return (m/3600)/N
print("cele top 4 frecvente sunt:")
for i in top4:
    print(f_a(i),"hz")

"""
cele top 4 frecvente sunt:
4.556722076407116e-08 hz
1.1574074074074073e-05 hz
3.037814717604744e-08 hz
1.518907358802372e-08 hz
"""
# prima corespunde la jumatate de an (0.69 ani) => schimbari de sezon
# a doua corespunde la o zi => schimbari de la zi la noapte
# a treia corespunde la 1.04 ani => schimbari de la an la an
# a patra corespunde la 2.09 ani => pentru ca setul de date este de 2 ani, acesta ar putea sa exprime cresterea overall

