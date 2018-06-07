#!/usr/bin/env python

from math import sqrt
from tabulate import tabulate

#-------------------------------------------------------------------------------------------#
# Function: mysqrt
# Description: determines the sqrt of a value
# Parameters: a
# Returns: the sqrt of the parameter
# Warnings: NA
#-------------------------------------------------------------------------------------------#
def mysqrt(a):

    x = a/2

    while True:
        
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

    return x

#-------------------------------------------------------------------------------------------#
# Function: test_square_root
# Description: prints a table of test values
# Parameters: the maximum value of the test (optional)
# Returns: NA
# Warnings: NA
#-------------------------------------------------------------------------------------------#
def test_square_root(z=9):
    print('a  mysqrt   math.sqrt   diff')

    # outer list will contain indicies of current value, btoh sqrts and the diff
    values =[]
    

    for i in range(1,z+1):

        # reset the inner list
        newVals = []

        # append the current value
        newVals.append(i)
        
        # calculate two sqrts and append to list
        newVals.append(mysqrt(i))
        newVals.append(sqrt(i))

        # calc different and append to list
        newVals.append(abs(newVals[1]-newVals[2]))

        # append the values to the outer list
        values.append(newVals)

    # print the list all fancy
    print(tabulate(values))


if __name__ == '__main__':

    # function call
    test_square_root()

    
