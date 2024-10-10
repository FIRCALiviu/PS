import scipy 
import numpy as np
import matplotlib.pyplot as plt

domeniu = np.array(range(100))

s = np.sin(4*np.array(range(100))+np.pi/2)
c = np.cos(4*np.array(range(100)))

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('cosinus este acelasi lucru cu sinus (cu pi/2 diferit) ')


ax1.plot(domeniu, s, 'o')
ax1.set_ylabel('Sinus sin(t+pi/2)')
ax2.plot(domeniu, c, 'o')
ax2.set_ylabel('Cosinus ')
#plt.show()


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
#plt.show()


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