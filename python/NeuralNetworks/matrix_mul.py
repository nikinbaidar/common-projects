#! /usr/bin/python

from os import system
from scipy import stats
from time import sleep

import numpy

## Create Data
system("clear")

# Input
x = numpy.arange(0,100,1).reshape(-1,1)
y = 10*x + 10
e = stats.norm.rvs(size=x.shape, scale=50, random_state=13)
y = y + e

m = len(y)
theta = numpy.zeros((2,1))

# getLoss wala function:
ssd=numpy.sum(numpy.square(x.dot(theta[1]) + theta[0] -y))/(2*m)

print(ssd)
