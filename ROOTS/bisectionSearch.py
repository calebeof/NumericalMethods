'''
Author: Calebe Oliveira
May, 2019.
'''

import numpy as np

#Simple function that we will use as an example

def x3_20(x):
    return x**3 - 20

def bisectionSearch(function, xMin, xMax, maxIt = 100, tolerance = 0.0001):
    '''
    The Bisection Search is an iterative method which use the following property:
    'If the product between f(x0) and f(x1) have a negative value, so there is a root in the interval between x0 and x1 in the function f.'
    So, the Bisection Search just initiate with two values, called xMin and xMax.
    Then, we get the middle of the interval [xMin,xMax] and do the verifications that we want.
    The verifications change the interval we are approaching, in order to approximate even more until we find a root (when the product between xMin and xMax is zero).
    The method also will check the tolerance and will stop if the differences between the roots will increase in a slow manner.
    Also, the Bisection Search have a logarithmical complexity, because of the consecutive divisions of intervals by two.
    '''
    errors = []
    roots = []

    if function(xMin)*function(xMax)>0:
        print("The root isn't isolated")
        return 

    for i in range (0, maxIt):
        
        #Getting the middle

        xMid = (xMax+xMin)/2
        roots.append(xMid)

        #Making the verifications that we need to change the intervals in order to a better approach

        if function(xMid)*function(xMax)<0:
            xMin = xMid
        elif function(xMin)*function(xMid)<0:
            xMax = xMid
        else:
            break
        
        #Comparing the values between the old roots and the new roots, in order to calculate the errors
        if i>0:
            actualError = abs((roots[-1]-roots[-2])/roots[-1])
            errors.append(actualError)
            
            if actualError<=tolerance:
                break

    return roots, errors

roots, errors = bisectionSearch(x3_20, 1, 4, tolerance = 0.0001)

#Printing the last root that we found
print('{:.6f}'.format(roots[-1]))