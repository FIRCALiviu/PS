import scipy 
import numpy as np
import matplotlib.pyplot as plt

# acuma ascultam semnalele

sem2a = np.sin(2*np.pi*400*np.arange(0,2,1/44100))
sem2b = np.sin(2*np.pi*800*np.arange(0,3,1/10000))
sem2c = np.arange(0,2,1/44100)%(1/240)*240
sem2d = np.sign(np.arange(0,2,1/44100)%(1/300)-1/600)

import sounddevice

sounddevice.play(sem2a,44100)
sounddevice.wait()
sounddevice.play(sem2b,10000)
sounddevice.wait()
sounddevice.play(sem2c,44100)
sounddevice.wait()
sounddevice.play(sem2d,44100)
sounddevice.wait()

from scipy.io.wavfile import write,read

write('sound.wav',44100,sem2a)

rate, x = read('sound.wav')

sounddevice.play(x,rate)
sounddevice.wait()