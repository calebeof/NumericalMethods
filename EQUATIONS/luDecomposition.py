'''
Author: Calebe Oliveira
May, 2019.
'''

import numpy as np 
from scipy.linalg import solve_triangular

np.set_printoptions(formatter={'float': lambda x: "{:.4f}".format(x)})

def checkDecompositionVeracity(L, U, matrix):
    if np.all(np.dot(L,U)==matrix):
        return "That's right!"
    return "That's not right!"

def checkInversionVeracity(matrix, matrixInverse):
    if np.all(np.dot(matrix, matrixInverse)==np.identity(matrix.shape[0])):
        return "That's right!"
    return "That's not right!"

def decomposition(matrix):
    L = np.identity(matrix.shape[0])
    U = np.array(matrix.copy(), dtype = float)

    for i in range (0, matrix.shape[0]-1):
        pivot = U[i, i]
        for j in range (i+1, matrix.shape[0]):
            mult = U[j,i]/pivot
            L[j, i] = mult
            U[j]-=(U[i]*mult)
    return L, U

def inversion(matrix):
    I = np.identity(matrix.shape[0])
    Z = np.zeros(matrix.shape[0])
    matrixInverse = np.zeros(matrix.shape)
    L,U = decomposition(matrix)
    
    print(checkDecompositionVeracity(L, U, matrix))

    for i in range (0, matrix.shape[0]):
        Z = solve_triangular(L, I[:,i], lower = True)
        matrixInverse[:, i] = solve_triangular(U, Z, lower = False)
    
    print(checkInversionVeracity(matrix, matrixInverse))

    return matrixInverse
    
A = np.array([[2,1], [-4, -6]], dtype = float)
B = np.array([[2,1,-4], [2,2,-2], [6,3,-11]], dtype = float)
C = np.array([[1,3,2],[2,8,5],[1,11,4]], dtype = float)

invA = inversion(A)
invB = inversion(B)
invC = inversion(C)
print(invA)
print(invB)
print(invC)
