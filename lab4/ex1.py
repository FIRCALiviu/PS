import numpy as np

def fourier(vec,m):
    n = len(vec)
    return (np.sum(vec*np.exp(-2*np.pi*1j*m/n*np.array(range(n)))))

def dft(vec):
    rez = []
    for i in range(len(vec)):
        rez.append(fourier(vec,i))
    return rez
import time
import os

if not os.path.exists('rez.txt'):

    teste = [128, 256, 512, 1024, 2048, 4096, 8192]
    timpi_dft= []
    timpi_fft = []
    for i in teste:
        test = np.random.randint(0,10,i)
        start  =time.time()
        
        f = np.fft.fft(test)
        end = time.time()
        timpi_fft.append(end-start)
    for i in teste:
        test = np.random.randint(0,10,i)
        start  =time.time()
        
        f = dft(test)
        end = time.time()
        timpi_dft.append(end-start)

    with open("rez.txt",'w') as file:
        file.write(" ".join(map(str,timpi_dft)))
        file.write('\n')
        file.write(" ".join(map(str,timpi_fft)))
else:
    with open("rez.txt") as file:
        timpi_dft =[float(x) for x in file.readline().split()]
        timpi_fft =[float(x) for x in file.readline().split()]

import matplotlib.pyplot as plt
plt.plot([128, 256, 512, 1024, 2048, 4096, 8192],timpi_fft,label= "fft")
plt.plot([128, 256, 512, 1024, 2048, 4096, 8192],timpi_dft,label = "dft python")
plt.yscale('log')
plt.legend()
plt.show()