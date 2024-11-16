import sounddevice

f  = 44100

t = 5

vocale = sounddevice.rec(f*t,samplerate=f,channels=1)

sounddevice.wait()

from scipy.io.wavfile import write

write("aeiou.wav",f,vocale)

# cum se vede pe spectrul fiecarei vocale, nu se poate determina vocala doar privind imaginea. 
# Dar daca ar fi mai putin zgomot in .wav, si am procesa mai mult (bine) datele, sunt sigur ca se poate decide

