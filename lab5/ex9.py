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

# Dupa ce m-am uitat la grafic, vreau sa pastrez doar 25% din primele valori, pentru ca dupa acea, nu mai erau tepe mari

filtrare = np.zeros(N).astype(np.complex128)
split = N//4
filtrare[:split] = np.fft.fft(data)[:split]

gata = np.fft.ifft(filtrare)

plt.plot(range(0,N),np.real(gata))
plt.show()