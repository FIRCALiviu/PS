import numpy as np ,matplotlib.pyplot as plt

first = np.sin(2*np.pi*10*np.arange(0,2,1/44100))
second = np.arange(0,2,1/44100)%(1/10)*10
domeniu = np.arange(0,2,1/44100)

fig ,(a,b,c) = plt.subplots(3,1)

a.plot(domeniu,first)
b.plot(domeniu,second)
c.plot(domeniu,first+second)
plt.show()