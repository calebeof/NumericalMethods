'''
Author: Calebe Oliveira
May, 2019.
'''

import numpy as np

#Setting the float numbers to 4 point precision
np.set_printoptions(formatter={'float': lambda x: "{:.4f}".format(x)})


def eliminationGauss(matrix):
    for i in range (0, matrix.shape[0]-1):
        '''
        Changing the idea of getting the pivot:
        Now, we change the pivot to the highest (absolute) number under the point in the actual column.
        After that, we swap the lines and continue the process with the new pivot. 
        It's easy to note that is better because we try to avoid the division by zero every time we choose a pivot now.
        '''
        maximum = i + np.argmax(abs(matrix[i:, i]))
        
        matrix[[maximum, i]] = matrix[[i, maximum]]

        #Continuing the process that we had in the naive process
        pivot = matrix[i, i]

        for j in range (i+1, matrix.shape[0]):
            multiplier = matrix[j,i]/pivot
            matrix[j]-=(matrix[i]*multiplier)

    return matrix

def substitutionGauss(matrix):
    
    #Same back substitution now, because we have an 

    roots = np.zeros(matrix.shape[0])

    for i in range (0, roots.shape[0]):

        sum = 0
        independent_coefficient = matrix[i, matrix.shape[1]-1]
        coefficient = matrix[i, i]

        for j in range (0, roots.shape[0]):
            sum+=(matrix[i, j]*roots[j])
        
        roots[i] = (independent_coefficient-sum)/coefficient

    return roots

'''
Example of a system of equations:
25x1 + 5x2 + x3 = 106.8
64x1 + 8x2 + x3 = 117.2
144x1 + 12x2 + 12x3 = 279.2
'''
system = np.array([[25, 5, 1, 106.8], [64, 8, 1, 177.2], [144, 12, 1, 279.2]], dtype = float)

#We have an augmented matrix here, where the last column is filled with independent terms. 

print(eliminationGauss(system))
print('roots: ', substitutionGauss(eliminationGauss(system)))
