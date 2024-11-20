import numpy as np

import matplotlib.pyplot as plt

import csv

file = open("Train.csv")

vec = list(csv.reader(file))

data = np.array(vec[1:])[:,2].astype(np.float32)

print(data)
procesare = np.abs(np.fft.fft(data))

N = 18288

plt.plot((1/3600)*np.arange(0,N//2,1)/N,procesare[:N//2])
plt.xlabel('frecventa Hz')
plt.savefig('ex4.png')
plt.show()