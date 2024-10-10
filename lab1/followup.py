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

"""
3. 
a. intervalul de timp intre 2 esantioane este 1/2000 secunde
b. Am putea folosi algoritmul lui hufmann pentru a comprima datele :)
dar daca datele sunt pur aleatorii, va fi nevoie de 4*3600*2000/8 = 3.6 MB

"""