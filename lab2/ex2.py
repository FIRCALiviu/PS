import scipy 
import numpy as np
import matplotlib.pyplot as plt

domeniu = np.array(range(100))

sin1= np.sin(1/4*np.array(range(100))+1)
sin2= np.sin(1/4*np.array(range(100))+2)
sin3= np.sin(1/4*np.array(range(100))+3)
sin4= np.sin(1/4*np.array(range(100))+4)

plt.figure()
plt.title("4 faze diferite")
plt.plot(domeniu,sin1)
plt.plot(domeniu,sin2)
plt.plot(domeniu,sin3)
plt.plot(domeniu,sin4)

def get_gamma(snr,z,x):
    return (np.sqrt(np.sum(x**2)))/(np.sqrt(snr)*np.sqrt(np.sum(z**2)))


z = np.random.normal(size=100)
freq_new = []
for snr in [0.1,1,10,100]:
    freq_new.append(sin1+get_gamma(snr,z,sin1)*z)
fig, axis = plt.subplots(5, 1)
fig.suptitle('snr si gamma')

for i in range(4):
    axis[i].plot(domeniu,freq_new[i])
axis[4].plot(domeniu,sin1)
plt.show()