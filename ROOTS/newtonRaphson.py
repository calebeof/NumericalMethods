'''
Author: Calebe Oliveira
May, 2019.
'''

import numpy as np

#Simple function that we will use as an example

def x3_20(x):
    return x**3 - 20

#Derivative of the function that we will use as an example

def difx3_20(x):
    return 3*(x**2)

def newtonRaphson(function, functionDiff, x0, maxIt = 100, tolerance = 0.0001):
    '''
    The Newton-Raphson method will use the formula:
    x[i] = x[i-1] - f(x[i-1])/f'(x[i-1])
    The formula above will aproximate the value of the root in the function f.
    So, we just need an initial value, the function and the function's derivative.
    Then, we just get in the iterative form, stopping when we get to a limit of tolerance error or iterations.
    '''
    errors = []
    roots = []
    
    #Saving the initial value as a possible root, or just our seed

    roots.append(x0)

    for i in range (0, maxIt):

        #Aplying the formula and saving
        
        roots.append(roots[-1] - (function(roots[-1])/functionDiff(roots[-1])))
        
        #Comparing the values and checking the tolerance
        
        if i>0:
            actualError = abs((roots[-1]-roots[-2])/roots[-1])
            errors.append(actualError)
            
            if actualError<=tolerance:
                break
    
    return roots, errors

roots, errors = newtonRaphson(x3_20,difx3_20, 4)

#Printing the last root that we found

print('{:.6f}'.format(roots[-1]))