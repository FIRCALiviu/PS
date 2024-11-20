import numpy as np
import matplotlib.pyplot as plt

N=100

x = np.random.random(N)
plt.plot(range(N),x)
plt.show()
for i in range(3):
    x = np.convolve(x,x)
    plt.plot(range(len(x)),x)
    plt.show()


# se observa ca vectorul devine foarte mare, si se apropie de o curba gausiana