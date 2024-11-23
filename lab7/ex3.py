import numpy as np, matplotlib.pyplot as plt
import scipy.misc as misc
X = misc.face(gray=True)
np.random.seed(0)
def snr(pic):
    
    rez= (pic-pic.min()+1).mean()/pic.std()
    
    return rez

threshold = 100000

pixel_noise = 200

noise = np.random.randint(-pixel_noise, high=pixel_noise+1, size=X.shape)
X_noisy = X + noise


spectru = np.abs(np.fft.fft2(X_noisy))
transform = np.fft.fft2(X_noisy)
transform[spectru<threshold]=0j
raton_filtrat =  np.real(np.fft.ifft2(transform))

plt.imshow(raton_filtrat,cmap= 'gray')
plt.savefig("raton filtrat ex3.png")
plt.show()

print(snr(X_noisy),snr(raton_filtrat))