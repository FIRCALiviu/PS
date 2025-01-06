import pickle,numpy as np,matplotlib.pyplot as plt
from scipy.fft import dctn, idctn
from PIL import Image
with open("compresed.pkl","rb") as f:
    padn = pickle.load(f)
    padm = pickle.load(f)
    n = pickle.load(f)
    m = pickle.load(f)
    rf = pickle.load(f) # rf : functia care ne da valoarea lui r (dictionar de la huffman)
    gf = pickle.load(f)
    bf = pickle.load(f)
    vec_r = pickle.load(f)
    vec_g = pickle.load(f)
    vec_b = pickle.load(f)
    intR  =  pickle.load(f)
    intG = pickle.load(f)

    intB = pickle.load(f)

# acum decriptam stringul de 0 si 1

def decrypt(integer:int,f:dict):
    
    s = bin(integer)[3:] # nu e bug : ignoram primul 1 care a fost adaugat ca padding

    vec = []
    considered_word = ""
    for ch in s:
        if considered_word+ch in f:
            vec.append(f[considered_word+ch])
            considered_word =""
        else:
            considered_word+=ch

    return vec

R = np.array(decrypt(vec_r,rf) if intR==10**8 else [intR]*n*m)
G = np.array(decrypt(vec_g,gf) if intG==10**8 else [intG]*n*m)
B = np.array(decrypt(vec_b,bf) if intB==10**8 else [intB]*n*m)
R = R.reshape(n,m)
G  = G.reshape(n,m)
B = B.reshape(n,m)

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

picture = np.dstack((R,G,B))

picture = ycc_itransform(picture)

picture[picture<0] = 0
picture[picture>255] = 255


picture = picture[:n-padn,:m-padm]
if True:
    image = Image.fromarray(picture.astype(np.uint8),mode='RGB')
    image.save('compressed.png')

# image = Image.fromarray(np.zeros_like(image).astype(np.uint8),mode='RGB')
# image.save('test<.png')