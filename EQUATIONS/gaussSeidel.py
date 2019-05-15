'''
Author: Calebe Oliveira
May, 2019.
'''

import numpy as np

#Setting the float numbers to 4 point precision
np.set_printoptions(formatter={'float': lambda x: "{:.4f}".format(x)})

def gaussSeidel(matrix, max_it = 100, tolerance = 0.0001):

    '''
    The idea of the Gauss-Seidel method is to execute the same back substitution that we have in the method proposed by Gauss, but now in 'front mode'.
    But now, this process turns out to be an iterative, and will iterate comparing the roots with the last ones, until surpass the limit of iterations or begin under the tolerance atributted.
    '''
    
    #Saving the new roots and the old roots
    newRoots = np.zeros(matrix.shape[0])
    oldRoots = np.zeros(matrix.shape[0])

    for i in range (0, max_it):
        
        #Doing the front substitution

        for j in range(0, newRoots.shape[0]):

            sum = 0
            independent_coefficient = matrix[j, matrix.shape[1]-1]
            coefficient = matrix[j, j]

            for k in range (0, newRoots.shape[0]):
                if j!=k:
                    sum+=(matrix[j, k]*newRoots[k])
            
            newRoots[j] = (independent_coefficient-sum)/coefficient

        #Comparing the values between the old roots and the new roots
        if i>0:
            errors = []
            for j in range (0, newRoots.shape[0]):
                errors.append(abs((newRoots[j]-oldRoots[j])/newRoots[j]))
            
            maxError = max(errors)
            
            if maxError<=tolerance:
                break

        #Saving the old roots
        
        oldRoots = newRoots.copy()
    
    return newRoots

def checkVeracity(matrix, roots):
    if np.all(np.dot(matrix[:,:-1], roots)):
        return "That's right!"
    return "That's not right!"

'''
Example of a system of equations:
3x1 - 0.1x2 - 0.2x3 = 7.85
0.1x1 + 7x2 + 0.3x3 = -19.3
0.3x1 - 0.2x2 + 10x3 = 71.4
'''

system = np.array([[3, -0.1, -0.2, 7.85], [0.1, 7, 0.3, -19.3], [0.3, -0.2, 10, 71.4]], dtype = float)

roots = gaussSeidel(system)
print('roots: ', roots)
print(checkVeracity(system, roots))