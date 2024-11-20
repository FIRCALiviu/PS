import numpy as np
size = 20

p1 = np.random.random(size)
p2 = np.random.random(size)

coeficienti = [0]*(2*size-1)

for i in range(size):
    for j in range(size):
        coeficienti[i+j]+=p1[i]*p2[j]
print(np.array(coeficienti))

complex = np.fft.fft(p1,2*size-1)*np.fft.fft(p2,2*size-1)
convolutie = np.real(np.fft.ifft(complex))

print(convolutie)