import numpy as np
import matplotlib.pyplot as plt
def x(t):
    return np.cos(520*np.pi*t+np.pi/3)

domeniu_esantionare = np.arange(0,1,1/200)
fig, axis = plt.subplots(1,1)
plt.stem(domeniu_esantionare,x(domeniu_esantionare))


plt.show()