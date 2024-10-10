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


semnal1 =lambda x: np.cos(2*np.pi*400*x)
dom = np.array(range(1600))/160
sam1 = semnal1(dom)
plt.plot(dom,sam1)
plt.show()
semnal2 = lambda x :np.cos(2*np.pi*800*x)
dom = np.arange(0,3,1/2400)
sam2 = semnal2(dom)

plt.plot(dom,sam2)
plt.show()
# de 240 hz
dom = np.arange(0,3,1/20000)
sawtooth = lambda x : (x % (1/240))
plt.plot(dom,sawtooth(dom))
plt.show()

square = lambda x : np.sign((x % (1/300))-1/600)
dom = np.arange(0,5,0.01)
plt.plot(dom,square(dom))
plt.show()

image = np.random.rand(128,128)
plt.imshow(image)
plt.show()


