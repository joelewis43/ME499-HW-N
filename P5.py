#!/usr/bin/env python

from math import tan
from math import degrees as deg
from math import radians as rad

class poly:

    # start here
    def __init__(self, n):
        self.n = n
        self.l = 1

        while self.n < 3:
            temp = input('Please enter number of sides greater than 3: ')
            self.n = int(temp)

    def area(self):
        # calculate the perimeter
        p = self.l * self.n

        # calculate inner value for a
        angle = rad(180/self.n)
        angle = tan(angle)

        # calculate the apothem (from wikihow.com)
        a = self.l / (2 * angle)

        # return the area
        return (a*p)/2

    def __str__(self):

        if self.n == 3:
            return "Triangle"
        elif self.n == 3:
            return "Square"
        elif self.n == 3:
            return "Pentagon"
        elif self.n == 3:
            return "Hexagon"
        else:
            return str(self.n) + '-sided Polygon'


    
if __name__ == '__main__':

    test = poly(2)
    print(test)
    print(test.area())
