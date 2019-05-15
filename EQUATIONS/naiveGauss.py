'''
Author: Calebe Oliveira
May, 2019.
'''

import numpy as np

#Setting the float numbers to 4 point precision
np.set_printoptions(formatter={'float': lambda x: "{:.4f}".format(x)})

def eliminationGauss(matrix):
    '''
    The process of elimination can get us an upper triangular matrix, in order to be simple to solve a system of equations.
    So, in fact, we have to create a matrix that have zeros under the main diagonal.
    A pivot is an element which we chose in the main diagonal in order to create a multiplier.
    The i-th multiplier will be the i-th element in the j-th row, which will have the value of matrix[j, i]/pivot. 
    After that, we will just subtract the j-th row with the product of the multipler and the i-th row.
    With this process, we can change the j-th equation (or j-th row) preserving its proportion and getting the zeros that we want at the beginning. 
    '''
    for i in range (0, matrix.shape[0]-1):
        pivot = matrix[i, i]
        for j in range (i+1, matrix.shape[0]):
            multiplier = matrix[j, i]/pivot
            matrix[j]-=(multiplier*matrix[i])

    return matrix

def substitutionGauss(matrix):
    '''
    Now that we have a upper triangular matrix, we can just rearrange the equations and substitute.
    In the end, we will find all the roots in the system. 
    This is a back substitution, because we begin to substitute the roots from the back (last equation) until the front (first equation).
    Basically, the independent term is subtracted from the sum of the product between all coefficients and your respectively roots (that are progressively being found).
    The root's coefficient that we are trying to find will divide all of this, and then we will find that root. 
    It's just a rearrangement of all equations to isolate the roots.
    '''
    roots = np.zeros(matrix.shape[0])
    
    for i in range (roots.shape[0]-1, -1, -1):
        sum = 0
        coefficient = matrix[i, i]
        independent_term = matrix[i, matrix.shape[1]-1]

        for j in range(0, roots.shape[0]):
            sum+=(matrix[i, j]*roots[j])
        
        roots[i] = (independent_term-sum)/coefficient
    
    return roots

def checkVeracity(matrix, roots):
    if np.all(np.dot(matrix[:,:-1], roots)):
        return "That's right!"
    return "That's not right!"
    
'''
Example of a system of equations:
25x1 + 5x2 + x3 = 106.8
64x1 + 8x2 + x3 = 117.2
144x1 + 12x2 + 12x3 = 279.2
'''

system = np.array([[25, 5, 1, 106.8], [64, 8, 1, 177.2], [144, 12, 1, 279.2]], dtype = float)

unreducedSystem = eliminationGauss(system)

#We have an augmented matrix here, where the last column is filled with independent terms. 

print(unreducedSystem)

roots = substitutionGauss(unreducedSystem)

print('roots: ',roots)

print(checkVeracity(unreducedSystem, system))