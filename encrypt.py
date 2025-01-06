import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn
image_name = 'image.png'

import cv2
img =cv2.imread(image_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

import numpy as np


Q_jpeg = [[16, 11, 10, 16, 24, 40, 51, 61],
          [12, 12, 14, 19, 26, 28, 60, 55],
          [14, 13, 16, 24, 40, 57, 69, 56],
          [14, 17, 22, 29, 51, 87, 80, 62],
          [18, 22, 37, 56, 68, 109, 103, 77],
          [24, 35, 55, 64, 81, 104, 113, 92],
          [49, 64, 78, 87, 103, 121, 120, 101],
          [72, 92, 95, 98, 112, 100, 103, 99]]
Q_jpeg = np.array(Q_jpeg,dtype=np.float64)

MSE = int(input("what is max MSE? :"))
def ycc_transform(picture_rgb):
    kg = 1/3
    kb = 1/3
    kr = 1/3
    kg = 1/3
    kb = 1/3

    tr = np.zeros((3,3))
    tr[0,0] = kr
    tr[0,1] = kg
    tr[0,2] = kb
    tr[1,0] = -1/2 *(kr/(1-kb))
    tr[1,1] = -1/2 *(kg/(1-kb))
    tr[1,2] = 1/2
    tr[2,0] = 1/2
    tr[2,1]  = -1/2 *(kg/(1-kr))
    tr[2,2] = -1/2 *(kb/(1-kr))
    shape = picture_rgb.shape
    

     
    return ((picture_rgb.reshape(-1,3))@(tr.T)).reshape(shape)

# transformata inversa
def ycc_itransform(picture_rgb):
    kr = 1/3
    kg = 1/3
    kb = 1/3
    tr = np.zeros((3,3))
    tr[0,0] = 1
    tr[0,1]= 0
    tr[0,2] =2-2*kr
    tr[1,0] = 1
    tr[1,1] =-kb/kg*(2-2*kb)
    tr[1,2] =-kr/kg*(2-2*kr)
    tr[2,0] = 1
    tr[2,1] = 2-2*kb
    tr[2,2] = 0
    
    shape = picture_rgb.shape
    return ((picture_rgb.reshape(-1,3))@(tr.T)).reshape(shape)

a  = np.random.randn(16*16)
a = a.reshape((16,16))
test = np.array( [[10**(i-j) for i in range(8)] for j in range(8)] )
def q_prod(a,matr):
    res = np.zeros_like(a)

    for i in range(len(a)):
        for j in range(len(a[0])):
            
            res[i,j] = a[i,j]*matr[i%8,j%8]
    return res
res = q_prod(a,test)

def verify(a,matr,res):
    for i in range(len(a)//8):
        for j in range(len(a[0])//8):
            print(np.allclose(a[i*8:(i+1)*8,j*8:(j+1)*8]*matr,res[i*8:(i+1)*8,j*8:(j+1)*8]))
if False: # testarea produsului
    verify(a,test,res)

def pad_matr(matr):
    oldr,oldc = matr.shape
    newr,newc=oldr,oldc
    if newr%8:
        newr -=newr%8
        newr +=8
    if newc%8:
        newc -=newc%8
        newc +=8
    padd = np.zeros((newr,newc))
    padd[:oldr,:oldc] = matr
    return padd


def q_and88dct(matr):
        batches = []
        n = len(matr)//8
        m = len(matr[0])//8
        for i in range(n):
            for j in range(m):
                batches.append(matr[8*i:8*(i+1),8*j:8*(j+1)])
        for i in range(len(batches)):
            d =  dctn(batches[i])
            d=Q_jpeg*np.round(d/Q_jpeg)
            d = idctn(d)
            batches[i] = d
        res = np.empty_like(matr,dtype=np.int32)
        for i in range(n):
            for j in range(m):
                res[8*i:8*(i+1),8*j:8*(j+1)] = batches[i*m+j] # truc din assembly / C
        return res 

###########
keep_going = True
last_iter = None # valoarea lui RGB cu MSE mai mic decat cel impus
MAX_ITER = 100

while keep_going and MAX_ITER!=0: # refacem algoritmul cu Q din ce in ce mai mare
    MAX_ITER -=1
    R,G,B = img[:,:,0],img[:,:,1],img[:,:,2]

    R = pad_matr(R)
    G = pad_matr(G)
    B = pad_matr(B)

    padded_img = np.dstack((R,G,B))

    ycc = ycc_transform(padded_img)
    # nu mai e rgb dar e acelasi lucru, acum poate sa ia valori negative/pozitive
    R,G,B = ycc[:,:,0],ycc[:,:,1],ycc[:,:,2]

    R = q_and88dct(R)
    G  = q_and88dct(G)
    B = q_and88dct(B)
    
    temp = np.dstack((R,G,B))
    temp = ycc_itransform(temp)
    temp[temp<0] = 0
    temp[temp>255] = 255
    if (error:=((temp-padded_img)**2).sum()) > MSE:
        keep_going = False
        break
    print(int(error))
    Q_jpeg*=1.2 # encriptie mai agresiva
    last_iter = R.copy(),G.copy(),B.copy()
#######


if last_iter is None: # daca algoritmul este prea gresit incat a dat return de la prima iteratie
    R_vec = R.reshape(-1)
    G_vec = G.reshape(-1)
    B_vec = B.reshape(-1)
else:
    R,G,B = last_iter
    R_vec = R.reshape(-1)
    G_vec = G.reshape(-1)
    B_vec = B.reshape(-1)
import huffman,collections


R_compress =  huffman.codebook(collections.Counter(R_vec).items())

G_compress =  huffman.codebook(collections.Counter(G_vec).items())


B_compress =  huffman.codebook(collections.Counter(B_vec).items())

vec_R="".join(map(lambda x: R_compress[x],R_vec))
vec_G ="".join(map(lambda x: G_compress[x],G_vec))
vec_B = "".join(map(lambda x: B_compress[x],B_vec))

R_decode = {j:int(i) for i,j in R_compress.items()}
G_decode = {j:int(i) for i,j in G_compress.items()}
B_decode = {j:int(i) for i,j in B_compress.items()}

m = img.shape


import pickle
with open('compresed.pkl','wb') as f:
    pickle.dump(R.shape[0]-m[0],f) # give padding
    pickle.dump(R.shape[1]-m[1],f) 
    pickle.dump(len(R),f) #dimensiune
    pickle.dump(len(R[0]),f)
    pickle.dump(R_decode,f)
    pickle.dump(G_decode,f)
    pickle.dump(B_decode,f)
    pickle.dump(int('1'+vec_R,2),f) # optimizare de memorie foarte ingenioasa 
                                    # trebuie adaugat un 1 ca sa nu manace zerourile de la inceput
    pickle.dump(int('1'+vec_G,2),f)
    pickle.dump(int('1'+vec_B,2),f)
    if len(R_decode)==1:
        pickle.dump(R_decode[''],f) # daca hufman are o singura valoare, da fail si transmite valoarea lui R
    else:
        pickle.dump(10**8,f)# nu cred ca poate matricea sa dea valori atat de mari
    if len(G_decode)==1:
        pickle.dump(G_decode[''],f) # acelasi lucru
    else:
        pickle.dump(10**8,f)
    if len(B_decode)==1:
        pickle.dump(B_decode[''],f)
    else:
        pickle.dump(10**8,f)