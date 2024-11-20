import numpy as np
import matplotlib.pyplot as plt
N=200
def gen_rectangular(dimensiune=N):
    return [1]*N
def get_hann(dimensiune=N):
    return 0.5*(1-np.cos(2*np.pi*np.array(range(0,N))/N))





from scipy.ndimage import generic_filter

def apply_filter(semnal,f,N):
    rez = []
    semnal  = semnal.copy()
    semnal = np.concatenate((np.zeros(N),semnal))
    for i in range(len(semnal)-N+1):
        rez.append((semnal[i:i+N]*f).sum())
    return rez
f = 100
s = np.sin(2*np.pi*f*np.arange(0,20,0.001))
print(s.max())
x = apply_filter(s,gen_rectangular(),N)

plt.plot(range(len(x)),x)

plt.show()

x = apply_filter(s,get_hann(),N)

plt.plot(x)
plt.show()