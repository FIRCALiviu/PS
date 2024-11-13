import numpy as np
import matplotlib.pyplot as plt

n = 7*10**3
freq = n
domain = np.arange(0,1,1/freq)
samples = np.sin(2*np.pi*20*domain) + np.sin(2*np.pi*60*domain)+np.sin(2*np.pi*7*domain)+np.sin(2*np.pi*75*domain)


def fourier(n,vec,m):
    return abs(np.sum(vec*np.exp(-2*np.pi*1j*m/n*np.array(range(n)))))


data = []
for m in range(n):
    data.append(fourier(n,samples,m))
data = np.array(data)


repr = np.array(range(n))

plt.stem(repr,data)
plt.xlim(right=80,left  =0) # frecventele sunt intre 7 si 75
plt.savefig("plot")
plt.show()