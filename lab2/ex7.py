import numpy as np, matplotlib.pyplot as plt

esantion  = np.cos(2*np.pi*200*np.arange(0,2,1/10000))
split = esantion[::4]
split2 = esantion[2::4]

fig ,(a,b,c) = plt.subplots(3,1)
domeniu  = np.arange(0,2,1/10000)
a.scatter(domeniu,esantion)
b.scatter(np.arange(0,2,2/len(split)),split)
c.scatter(np.arange(0,2,2/len(split2)),split2)
plt.show()
# cu atat esantionam mai putin, cu atat seamana mai putin cu o frecventa sinus
