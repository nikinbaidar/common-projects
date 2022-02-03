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

x = numpy.hstack((numpy.ones((x.shape[0],1)),x))

alpha = 0.00001
losses = []
number_of_iterations = 200

theta = numpy.zeros((2,1))

for i in range(number_of_iterations):
    prediction = x.dot(theta)

    # Calculating the loss
    delta = prediction - y
    delta_squared = numpy.square(delta)
    loss = 1/(2*m) * numpy.sum(delta_squared)
    losses.append(loss)

    for j in range(theta.shape[0]):
        theta[j] -= alpha/m * numpy.sum((delta * x[:,j].reshape(-1,1)))

    # if i > 0 and abs(losses[i] - losses[i-1]) <= 0.005:
    #     print("The loop stopped after {} iterations".format(i))
    #     break

print("The first value for loss:", losses[0] )
print("The final value for loss:", losses[-1] )

print("The final values for theta i.e. theta*: ", theta)

# Plot the losses!

pyplot.plot(losses, label = "Losses over Iterations" , color='r')
pyplot.xlabel("Iterations")
pyplot.ylabel("Losses")
pyplot.legend()
pyplot.show()

