# grupam datele in felul urmator generam 100 de buacti de timp, si fiecare bucata este alipita cu 25% din vecinul din stanga , si 25% din dreapta

from scipy.io.wavfile import read
import numpy as np

def spectru(v):
    return np.log10(np.abs(np.fft.fft(v))+1)

f, data = read("aeiou.wav")
l = len(data)

frame_size = l//100
if l %100 :
    data=data[:(l//100)*100] # trim last bits so it is modulo 100
data = data.tolist()
bins = [data[i*100:(i+1)*100] for i in range(100)]

rez = []
rez.append(bins[0]+bins[1][:50])
for i in range(1,99):
    rez.append(bins[i-1][75:]+bins[i]+bins[i][:25])

rez.append(bins[98][50:]+bins[99])



columns = list(map(spectru,rez))

matr = np.empty((len(rez[0]),100))

for i in range(100):
    for j in range(len(rez[0])):
        matr[j][i] = rez[i][j]
import matplotlib.pyplot as plt


plt.ylabel('frecventa (max=44100hz)')
plt.xlabel('tims (5 secunde)')
plt.imshow(matr,cmap= 'hot',)
plt.savefig("ex6.png")
plt.show()