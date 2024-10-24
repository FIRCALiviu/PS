import matplotlib.pyplot as plt
import numpy as np
domain = np.array(range(200))
semnal1 = np.sin(2*np.pi*domain)
semnal2 = np.sin(2*np.pi*2*domain)
semnal3 = np.sin(2*np.pi*4*domain)


plt.scatter(domain,semnal1)

plt.scatter(domain,semnal2)

plt.scatter(domain,semnal3)
plt.title('1e-13, practic sunt toate 0')
plt.show()