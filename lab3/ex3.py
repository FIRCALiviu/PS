import numpy as np
import matplotlib.pyplot as plt

n = 10**4
freq = n/5
domain = np.arange(0,5,1/freq)
samples = np.sin(2*np.pi*20*domain) + np.sin(2*np.pi*60*domain)+np.sin(2*np.pi*7*domain)+np.sin(2*np.pi*75*domain)


def fourier(n,vec,m):
    return np.abs(np.sum(vec*np.exp(-2*np.pi*1j*m/n*np.array(range(n)))))


data = []
for m in range(n):
    data.append(fourier(n,samples,m))

repr = np.array(range(n))
plt.stem(repr,data)
plt.show()