import matplotlib.pyplot as plt
import numpy as np
domain = np.array(range(200))*1/8
semnal1 = np.sin(2*np.pi*domain)
semnal2 = np.sin(2*np.pi*2*domain)
semnal3 = np.sin(2*np.pi*4*domain)


plt.scatter(domain,semnal1)

plt.scatter(domain,semnal2)

plt.scatter(domain,semnal3)
plt.title('sampling cu 8hz, X2 mai mare ca max')
plt.show()
# ex 4 : frecventa max este 200hz, din acest motiv trebuie sa facem sampling de macar 400hz
