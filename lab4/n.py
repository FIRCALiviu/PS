import numpy as np

domain = np.array(range(10))


vec = np.cos(2*np.pi*domain/10)

print(np.imag(np.fft.fft(vec)))