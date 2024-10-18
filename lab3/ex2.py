import matplotlib.pyplot as plt
import numpy as np

semnal = np.sin(np.pi*2*30*np.linspace(0,10,30*100))

freq = [30,15,25,100,60]

for f in freq:
    floare = semnal*np.exp(-2*np.pi*1j*f*np.linspace(0,10,30*100))
    X = np.real(floare)
    Y = np.imag(floare)
    plt.scatter(X,Y,c = np.sqrt(X**2+Y**2))
    
    
    plt.savefig(f'ex2 cu frecventa w ={f}, f=30.png')
    plt.show()

