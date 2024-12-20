from ex12 import *
import numpy.linalg as la

prima = X@(X.T)
doua = (X.T)@X

eigenval_1, eigenvec_1 = la.eig(prima)
eigenval_2, eigenvec_2 = la.eig(doua)

eigenval_1 = np.real(eigenval_1)

eigenvec_1 = np.real(eigenvec_1)
eigenvec_2 = np.real(eigenvec_2)

eigenvec_2 = np.abs(eigenvec_2)
eigenvec_1 = np.abs(eigenvec_1)
u_svd,sigma_svd,v_svd=  la.svd(X)
u_svd = np.abs(u_svd)
v_svd = np.abs(v_svd)





eigenval_2 = np.real(eigenval_2)



vec1 = eigenvec_1.reshape(-1)
vec2 = u_svd.reshape(-1)

vec3 = eigenvec_2.reshape(-1)
vec4 = v_svd.reshape(-1)

vec1.sort()
vec2.sort()
vec3.sort()
vec4.sort()


eigenval_1.sort()

print(((vec1-vec2)**2).sum())
print(((vec3-vec4)**2).sum())
print(((eigenval_1[::-1]-sigma_svd**2)**2).sum())

print("relatiile sunt evidente : u = u si v = v in ambii algoritmi si in plus lambda = sigma*sigma ")