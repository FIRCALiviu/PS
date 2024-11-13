import numpy as np, matplotlib.pyplot as plt
fs = 1000
first = np.sin(2*np.pi*500*np.arange(0,2,1/fs))
second = np.sin(2*np.pi*250*np.arange(0,2,1/fs))
third = np.ones(fs*2)

fig ,(a,b,c) = plt.subplots(3,1)
domeniu  = np.arange(0,2,1/fs)
a.plot(domeniu,first)
b.plot(domeniu,second)
c.plot(domeniu,third)
plt.show()
# se observa ca esantionarea arata foarte prost cand f  = fs/2, dar foarte bine cand f = fs/4, daca avem 0hz, orice esantionare ar fi destul
