#!/usr/bin/env python

from random import uniform as rand
from math import pi

#-------------------------------------------------------------------------------------------#
# Function: estPi
# Description: estimates the value of pi with Monte Carlo Integration
# Parameters: the number of trials (defaults to 100000)
# Returns: the estimate of pi
# Warnings: NA
#-------------------------------------------------------------------------------------------#
def estPi(res=100000):

    # will count the number of random points within the circle
    count = 0

    # run this test the number of times specified
    for i in range(res):

        # generate and store a random number for x and y between -1 and 1
        x = rand(-1,1)
        y = rand(-1,1)

        # if the distance from the origin to the point
        # is less than the radius, the point is within
        # the circle
        if (x**2 + y**2 <= 1):
            count += 1

    # procedure from http://mathfaculty.fullerton.edu/mathews/n2003/montecarlopimod.html
    return (count/res) * 4
    

    


if __name__ == '__main__':

    a = estPi(100000000)
    print(a)
    print(pi)
    print(abs(a-pi))
    
