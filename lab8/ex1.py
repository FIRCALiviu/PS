import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,1000)
trend = X*X+X-5

sezon = np.sin(2*np.pi*2*X)+np.sin(2*np.pi*40*X)

rezidual = np.random.randn(1000)

serie = trend+sezon+rezidual/100

fig,axis = plt.subplots(4)

axis[0].plot(X,sezon)
axis[0].set_title('sezon')

axis[1].plot(X,trend)
axis[1].set_title('trend')

axis[2].plot(X,rezidual)
axis[2].set_title("rezidual")

axis[3].plot(X,serie)
axis[3].set_title('observed')

plt.show()

