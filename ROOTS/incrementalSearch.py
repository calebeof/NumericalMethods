'''
Author: Calebe Oliveira
May, 2019.
'''

import numpy as np 

#Simple function that we will use as an example

def sen10_cos3(x):
    return np.sin(10*x)+np.cos(3*x)

def incrementalSearch(function, xMin, xMax, jump = 0.1):
    '''
    The Incremental Search is an iterative method which use the following property:
    'If the product between f(x0) and f(x1) have a negative value, so there is a root in the interval between x0 and x1 in the function f.'
    So, the Incremental Search just initiate with two values, called xMin and xMax.
    Then, we brute force all the sub-intervals in the interval [xMin, xMax] with some jump values. 
    The sub-interval will be defined as [xi, xi+jump]. 
    If the property above it's satisfied, then we save that sub-interval that have potential roots.
    '''
    x = np.arange(xMin, xMax, jump)
    subIntervals = []

    for xi in x:
        if function(xi)*function(xi+jump) < 0:
            subIntervals.append((xi, xi+jump))
    
    return subIntervals

subIntervals = incrementalSearch(sen10_cos3, 3, 6, 0.01)
#Printing the sub-intervals that we found
print('{} sub-intervals found: \n {}'.format(len(subIntervals), subIntervals))