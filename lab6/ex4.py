timp = 24*3 # 3 zile

import matplotlib.pyplot as plt
import csv
import numpy as np

file = open("Train.csv")

d = list(csv.reader(file))[1:]
data = np.array(d)[:,2].astype(np.float64)
data = data[:timp]
plt.plot(data,label='original')
for w in (5,9,13,17):
    conv = np.convolve(data, np.ones(w), 'valid') / w
    
    plt.plot(conv,label = "w={}".format(w))
plt.legend()
plt.savefig('ex4b.png')
plt.show()

"""
O sa luam frecventele sub 50% din ele. In ultimul laborator am luat 25%, si pierderea de date era deja vizibila.
Nyquist frequency = 1/2*fs => ar avea 1/7200 HZ, si normalizat ar fi 1.

"""


