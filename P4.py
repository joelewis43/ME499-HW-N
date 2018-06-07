#!/usr/bin/env python

from random import uniform as rand

#-------------------------------------------------------------------------------------------#
# Function: mysqrt
# Description: determines the sqrt of a value
# Parameters: a
# Returns: the sqrt of the parameter
# Warnings: NA
#-------------------------------------------------------------------------------------------#
def probTest(a):

    count = 0
    total = a

    for i in range(total):

        first = rand(0, 1)
        second = rand(0, 1)

        if first < second:
            count += 1

    print(count/total * 100)

    


if __name__ == '__main__':

    
    probTest(100)
    probTest(1000)
    probTest(10000)
    probTest(100000)
    probTest(1000000)
    
