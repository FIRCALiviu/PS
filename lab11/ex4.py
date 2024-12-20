from ex12 import X,l
import numpy as np
u,sigma,v = np.linalg.svd(X)




def hankelizare(matr):
    n = len(matr)
    for i in range(n):
        s=0
        for j in range(i+1):
            s+=matr[i-j][j]
        for j in range(i+1):
            matr[i-j][j]=s/(i+1)
    for row in range(1, n):
        s=0
        r, c = row, n - 1
        while r < n and c >= 0:
            s+=matr[r,c]
            r += 1
            c -= 1
        
        r, c = row, n - 1

        while r < n and c >= 0:
            matr[r,c]=s/(n-row)
            r += 1
            c -= 1


v = v.T # V.T[:,i] != V[:,i].T
matricele =np.array( [sigma[i] * np.outer(u[:,i], v[:,i]) for i in range(0,l)] )
for m in matricele:
    hankelizare(m)
print(((X-matricele.sum(axis=0))**2).sum()) # note nu este necesar sa hankelizezi ca suma sa dea X