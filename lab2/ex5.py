import numpy as np, sounddevice

first = np.sin(2*np.pi*250*np.arange(0,2,1/44100))
second = np.sin(2*np.pi*500*np.arange(0,2,1/44100))
sound = np.append(first,second)

sounddevice.play(sound,44100)
sounddevice.wait()
#se remarca ca sunetul este mult mai acut
