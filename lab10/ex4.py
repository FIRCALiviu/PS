import numpy as np
def get_companion(coeff):
    matr = np.identity(len(coeff)-1)
    first_row = [0]*(len(coeff)-1)
    matr = np.concat(([first_row],matr),axis=0)
    matr = np.concatenate((matr,-coeff.reshape(-1,1)),axis=1)
    return matr
def get_roots(coeff):
    coeff = np.array(coeff)
    companion = get_companion(coeff)
    roots,_=np.linalg.eig(companion)
    return roots

