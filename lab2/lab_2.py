import scipy 
import numpy as np
import matplotlib.pyplot as plt

# acuma ascultam semnalele

sem2a = np.sin(2*np.pi*400*np.arange(0,2,1/44100))
sem2b = np.sin(2*np.pi*800*np.arange(0,3,1/10000))
sem2c = np.arange(0,2,1/44100)%(1/240)*240
sem2d = np.sign(np.arange(0,2,1/44100)%(1/300)-1/600)

import sounddevice

# sounddevice.play(sem2a,44100)
# sounddevice.wait()
# sounddevice.play(sem2b,10000)
# sounddevice.wait()
# sounddevice.play(sem2c,44100)
# sounddevice.wait()
# sounddevice.play(sem2d,44100)
# sounddevice.wait()

from scipy.io.wavfile import write,read

# write('sound.wav',44100,sem2a)

# rate, x = read('sound.wav')

# sounddevice.play(x,rate)
# sounddevice.wait()
first = np.sin(2*np.pi*10*np.arange(0,2,1/44100))
second = np.arange(0,2,1/44100)%(1/10)*10
domeniu = np.arange(0,2,1/44100)

fig ,(a,b,c) = plt.subplots(3,1)

a.plot(domeniu,first)
b.plot(domeniu,second)
c.plot(domeniu,first+second)
plt.show()

first = np.sin(2*np.pi*250*np.arange(0,2,1/44100))
second = np.sin(2*np.pi*500*np.arange(0,2,1/44100))
sound = np.append(first,second)

# sounddevice.play(sound,44100)
# sounddevice.wait()
# se remarca ca sunetul este mult mai acut

fs = 1000
first = np.sin(2*np.pi*500*np.arange(0,2,1/fs))
second = np.sin(2*np.pi*250*np.arange(0,2,1/fs))
third = np.ones(fs*2)

fig ,(a,b,c) = plt.subplots(3,1)
domeniu  = np.arange(0,2,1/fs)
a.plot(domeniu,first)
b.plot(domeniu,second)
c.plot(domeniu,third)
plt.show()
# se observa ca esantionarea arata foarte prost cand f  = fs/2, dar foarte bine cand f = fs/4, daca avem 0hz, orice esantionare ar fi destul

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
