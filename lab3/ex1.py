import math as mt
import numpy as np

M = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for k in range(8):
        M[i][k] = np.exp(-2*np.pi*1j*i*k/8)

import matplotlib.pyplot as plt

real = [[x.real for x in line] for line in M]

plt.imshow(real)
plt.show()
plt.imsave('Matricea ex1 real.png',real,cmap = 'gray')

imag = [[x.imag for x in line] for line in M]

plt.imshow(imag)
plt.show()
plt.imsave('Matricea ex1 imag.png',imag,cmap ='gray')

def modul(x):
    return np.sqrt(x.real**2+x.imag**2)

transpose = [[M[j][i].conj() for i in range(8) ] for j in range(8)]

res = np.array(transpose)@np.array(M)
magnitude = [[modul(res[i][j]) for i in range(8)] for j in range(8)]

plt.imshow(magnitude,cmap='grey')
plt.show()
print(np.allclose(res/res[0][0],np.identity(8)))

fig, axis = plt.subplots(8)



for i,line in enumerate(M):
    axis[i].plot(range(8),np.real(line),label='real')
    axis[i].plot(range(8),np.imag(line),label='imag')
    axis[i].legend()
plt.show()
