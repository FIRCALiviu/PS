import numpy as np

import matplotlib.pyplot as plt





import numpy as np
import matplotlib.pyplot as  plt
matr = np.zeros((128,128))
for i in range(-64,64):
    for j in range(-64,64):
        matr[i+64][j+64] = np.sqrt(i**2+j**2)
image = np.array(matr)

s = image.std()
gaussian = lambda x : 1/(np.sqrt(2*np.pi))*np.exp(-x**2/2/s)/s

plt.imshow(gaussian(image))
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