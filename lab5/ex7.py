# 2952 cade pe 26-12-2012 00, care este luni

import numpy as np

import matplotlib.pyplot as plt

import csv

file = open("Train.csv")

vec = list(csv.reader(file))

data = np.array(vec[1:])[:,2].astype(np.float32)

esantion = data[2952:3953]

plt.plot(range(2952,3953),esantion)
plt.xlabel('esantion')
plt.savefig("ex7.png")
plt.show()
