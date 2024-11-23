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
Nyquist frequency = 1/2*fs => ar avea 1/7200 HZ, si frecventa normalizata ar fi 0.5.

"""

order = 5
wn = 0.5 # 100% din nyquist frequency
rp = 5

from scipy.signal import butter, cheby1, sosfilt

filtru1 = butter(order,wn,output='sos')

filtru2 = cheby1(order,rp,wn,output='sos')

filtered1 = sosfilt(filtru1,data)
filtered2 = sosfilt(filtru2,data)

fig,axes = plt.subplots(3)

axes[0].plot(data)
axes[0].set_title("Date nefiltrate")

axes[1].plot(filtered1)
axes[1].set_title("Filtrate cu butter")

axes[2].plot(filtered2)
axes[2].set_title("Filtrate cu cheby1")

fig.suptitle("scara timp: 1 = 1 ora")
plt.savefig("butter si cheby.png")
plt.show()
# mie imi place mai mult cea filtrata cu butter, pentru ca altitudinea peakurilor este mai fidela la datele originale


# reproiectam filtrele cu ordini diferiti:

order = 2
wn = 0.5 # 100% din nyquist frequency
rp = 5

from scipy.signal import butter, cheby1, sosfilt

filtru1 = butter(order,wn,output='sos')

filtru2 = cheby1(order,rp,wn,output='sos')

filtered1 = sosfilt(filtru1,data)
filtered2 = sosfilt(filtru2,data)

fig,axes = plt.subplots(3)

axes[0].plot(data)
axes[0].set_title("Date nefiltrate")

axes[1].plot(filtered1)
axes[1].set_title("Filtrate cu butter")

axes[2].plot(filtered2)
axes[2].set_title("Filtrate cu cheby1")

fig.suptitle("scara timp: 1 = 1 ora")
plt.savefig("butter si cheby cu ordin =2.png")
plt.show()

order = 10
wn = 0.5 # 100% din nyquist frequency
rp = 5

from scipy.signal import butter, cheby1, sosfilt

filtru1 = butter(order,wn,output='sos')

filtru2 = cheby1(order,rp,wn,output='sos')

filtered1 = sosfilt(filtru1,data)
filtered2 = sosfilt(filtru2,data)

fig,axes = plt.subplots(3)

axes[0].plot(data)
axes[0].set_title("Date nefiltrate")

axes[1].plot(filtered1)
axes[1].set_title("Filtrate cu butter")

axes[2].plot(filtered2)
axes[2].set_title("Filtrate cu cheby1")

fig.suptitle("scara timp: 1 = 1 ora")
plt.savefig("butter si cheby cu ordin = 10.png")
plt.show()

# mie mi-a placut cel mai mult cheby cu ordin mic, pentru ca pozitia peakurilor este conservata cat mai bine, 
# dar frecventele mari sunt inca atenuate