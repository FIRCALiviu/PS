import numpy as np
import matplotlib.pyplot
import matplotlib.pyplot as plt
from scipy import misc
def snr(pic):
    
    rez= (pic-pic.min()).mean()/pic.std()
    
    return rez
def filter(pic,snr_threashold):
    spectru = np.abs(np.fft.fft2(pic))
    
    spectru_vec = spectru.reshape(-1)
    vals = spectru_vec.argsort()[np.array([9999*len(spectru_vec)//10000 + int( i/100*len(spectru_vec)//10000 ) for i in range(100)])]
    
    filtre = spectru_vec[vals]
    
    for threshold in filtre:
        print(threshold)
        transform = np.fft.fft2(pic)
        transform[spectru<threshold]=0
        raton_filtrat =  np.real(np.fft.ifft2(transform))
        if snr(raton_filtrat) > snr_threashold:
            return raton_filtrat
    print('failed filter')
    return raton_filtrat

raton = misc.face(gray=True)

plt.imshow(rez:=filter(raton,5),cmap='gray')
print(snr(rez))
plt.savefig("raton fara zgomot.png")
plt.show()