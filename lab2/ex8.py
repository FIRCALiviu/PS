import matplotlib.pyplot as plt
import numpy as np

domeniu = np.linspace(-np.pi/2,np.pi/2,10000)

plt.plot(domeniu,domeniu,label = 'id(x)')
plt.plot(domeniu,np.sin(domeniu),label = "sin(x)")
plt.plot(domeniu,(np.sin(domeniu)-domeniu)**2,label = "eroare patratica")
plt.legend(loc='upper center')
plt.show()

def pade(x):
    return (x-7*x**3/60)/(1+x**2/20)

plt.plot(domeniu,pade(domeniu),label = 'pade')
plt.plot(domeniu,np.sin(domeniu),label = 'sin')
plt.legend()
plt.yscale('log')
plt.show()

diff = np.log(np.abs( pade(domeniu) - np.sin(domeniu))+10**-10)

plt.plot(domeniu,diff,label= '|pade-sin| Diferenta maxima = 10 ^ -5')
plt.legend()
plt.show()