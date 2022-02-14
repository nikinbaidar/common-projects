#! /usr/bin/python

import numpy
from scipy import stats
from matplotlib import pyplot

# Input
x = numpy.arange(0,100,1).reshape(-1,1)

# Output
y = 10*x + 10
# add random errors to the output
e = stats.norm.rvs(size=x.shape, scale=50, random_state=13)
y = y + e

# print("x: ", x)
# print("y: ", y)

m = len(y) # number of samples

alpha = 0.00001
losses = []
number_of_iterations = 200

theta = numpy.zeros((2,1))

for i in range(number_of_iterations):
    prediction = theta[0] + x * theta[1]

    # Calculating the loss
    delta = prediction - y
    delta_squared = numpy.square(delta)
    loss = 1/(2*m) * numpy.sum(delta_squared)
    losses.append(loss)

    theta[0] -= alpha/m * numpy.sum((delta))
    theta[1] -= alpha/m * numpy.sum((delta * x))

print("The final values for theta i.e. theta*: ", theta)
