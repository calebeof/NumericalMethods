import numpy as np

#Simple function that we will use as an example

def polynomium(x):
    return x**3 - 6*(x**2) + 11*x - 6.1

def secant(function, x0, x1, maxIt = 100,tolerance = 0.0001):
    '''
    The Secant method will use the formula:
    x[i] = x[i-1] - f(x[i-1])*(x[i-1]-x[i-2])/(f(x[i-1])-f(x[i-2]))
    The formula above will aproximate the value of the root in the function f.
    So, we just need two values (x0 and x1) and the function.
    Then, we just get in the iterative form, stopping when we get to a limit of tolerance error or iterations.
    '''
    roots = []
    errors = []

    #Saving x0 and x1 as possible roots
    
    roots.append(x0)
    roots.append(x1)

    for i in range (0, maxIt):
        
        #Dividing the formula in numerator and denominator, in order to simplify the code 

        numerator = function(roots[-1])*(roots[-1] - roots[-2])
        denominator = function(roots[-1]) - function(roots[-2])
        
        roots.append(roots[-1] - (numerator/denominator))
        
        #Comparing the values between the old roots and the new roots, in order to calculate the errors

        if i>0:
            errorActual = abs((roots[-1]-roots[-2])/roots[-1])
            errors.append(errorActual)

            if errorActual<=tolerance:
                break
    
    return roots, errors

roots, errors = secant(polynomium, 2.5, 3.5) 

#Printing the last root that we found

print('{:.6f}'.format(roots[-1]))