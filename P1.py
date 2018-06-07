#!/usr/bin/env python

#-------------------------------------------------------------------------------------------#
# Function: is_power
# Description: determines if a value, a, is a power of a base, b.
# Parameters: a, b
# Returns: true if a is a power of b or false otherwise
# Warnings: NA
#-------------------------------------------------------------------------------------------#
def is_power(a, b):

    # not a power
    if a % b != 0:
        return False
    # values finally returned proof that it is a power
    elif a == b:
        return True
    # could still be a power, more testing needed
    else:
        return is_power(a/b, b)


if __name__ == '__main__':

    # function call
    print(is_power(6, 2))

    
