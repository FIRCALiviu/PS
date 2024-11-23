import numpy as np
import matplotlib.pyplot as plt

n1 = 200
n2 = 200
x1 = np.zeros((n1,n2))
for i in range(n1):
    
    for j in range(n2):
        x1[i][j] = np.sin(2*np.pi*i+3*np.pi*j)
plt.imshow(x1,cmap='gray')
plt.savefig("sinus ex1a.png")
plt.imshow(np.log10(abs(np.fft.fft2(x1))),cmap='gray')
plt.savefig("spectru ex1a.png")

# spectrul are sens, pentru ca si imaginea de baza are multe repetitii, are nevoie doar de anumite frecvente

n1= 100
n2 =100

x2= np.zeros((n1,n2))
for i in range(n1):
    for j in range(n2):
        x2[i][j] = np.sin(4*np.pi*i)+np.cos(6*np.pi*j)


plt.imshow(x2,cmap='gray')
plt.savefig("sinus si cos ex1b.png")
plt.imshow(np.log10(abs(np.fft.fft2(x2))+1),cmap='gray')
plt.savefig("spectru ex1b.png")

# cum se poate vedea, imaginea este super usor de comprimat, pentru ca arata mult ca un sinus vertical. Din cauza asta, FFT are nevoie de foarte putine valori, 
# din cauza asta numai un patrat mic sus stanga este aprins.

N = 100

Y1  = np.zeros((N,N))
Y1[0][5] = 1
Y1[0][N-5] = 1


plt.imshow(Y1,cmap='gray')
plt.savefig("Y ex1c.png")

plt.imshow(np.log10(abs(np.fft.fft2(Y1))+1),cmap='gray')
plt.savefig("spectru ex1c.png")

# are sens sa avem o functie sinus care iese in spectru, pentru ca fft este "propria sa inversa", daca aplicam fft pe sinus, ne asteptam sa avem (niste) puncte, 
# daca o aplicam pe niste puncte, (un punct de ex.) atuncea ne asteptam sa obtinem un sinus in return.


N = 100

Y1  = np.zeros((N,N))
Y1[5][0] = 1
Y1[N-5][0] = 1


plt.imshow(Y1,cmap='gray')
plt.savefig("Y ex1d.png")

plt.imshow(np.log10(abs(np.fft.fft2(Y1))+1),cmap='gray')
plt.savefig("spectru ex1d.png")
# are sens ca acest spectru sa fie cel de mai intai, dar rotit 90 de grade, pentru ca si imaginea folosita 
# este aceasi, dar rotita 90 de grade


N = 100

Y1  = np.zeros((N,N))
Y1[5][5] = 1
Y1[N-5][N-5] = 1

plt.imshow(Y1,cmap='gray')
plt.savefig("Y ex1e.png")

plt.imshow(np.log10(abs(np.fft.fft2(Y1))+1),cmap='gray')
plt.savefig("spectru ex1e.png")
# practic, am rotit spectrul cu 45 de grade, pentru ca si punctele au fost rotite cu 45 de grade.