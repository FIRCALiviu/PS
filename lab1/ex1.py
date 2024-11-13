import numpy as np

import matplotlib.pyplot as plt
def x(t):
    return np.cos(520*np.pi*t+np.pi/3)
def y(t):
    return np.cos(280*np.pi*t-np.pi/3)
def z(t):
    return np.cos(120*np.pi*t+np.pi/3)

n =  int(0.03/0.0005)

domeniu = np.linspace(0,0.03,n)

fig, axis = plt.subplots(3,1)
axis[0].plot(domeniu,x(domeniu))
axis[0].set_ylabel('x')

axis[1].plot(domeniu,y(domeniu))
axis[1].set_ylabel('y')
axis[2].plot(domeniu,z(domeniu))
axis[2].set_ylabel('z')
#plt.show()

domeniu_esantionare = np.arange(0,0.3,1/200) # 200 hz

fig, axis = plt.subplots(3,1)
axis[0].stem(domeniu_esantionare,x(domeniu_esantionare))
axis[0].set_ylabel('x')

axis[1].stem(domeniu_esantionare,y(domeniu_esantionare))
axis[1].set_ylabel('y')
axis[2].stem(domeniu_esantionare,z(domeniu_esantionare))
axis[2].set_ylabel('z')
plt.show()
