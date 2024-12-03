import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,100)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(100)

serie = trend+sezon+rezidual
