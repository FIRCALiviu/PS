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
plt.show()