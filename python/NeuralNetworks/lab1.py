#! /usr/bin/python

import numpy
from   scipy      import stats
from   matplotlib import pyplot

def getSampleLength(y):
    ''' Returns the value of m '''
    return len(y)

def getLinearPrediction(x, theta):
    ''' Remember:
        Dimensions of x = (m,n+1)
        Dimensions of theta = (n+1,1)
    '''
    return numpy.dot(x,theta)

def getLoss(x, y, theta):
    ''' Add a description '''
    totalDataPoints = getSampleLength(y)
    predicted_output = getLinearPrediction(x, theta)
    delta = predicted_output - y
    sumSquaredDifferences = numpy.sum(numpy.square(delta))
    loss = 1/2 * (sumSquaredDifferences/totalDataPoints)
    return loss

def getLinearGradient(x, y, theta):
    ''' Add a description '''
    # This feels redundant so maybe optimize in future
    totalDataPoints = getSampleLength(y)
    prediction = getLinearPrediction(x, theta)
    delta = prediction - y

    # Init a gradient array with same dimensions as theta
    gradient = numpy.zeros(theta.shape)

    for j in range(theta.shape[0]):
        gradient[j] = numpy.sum((delta * x[:,j].reshape(-1,1)))/totalDataPoints

    return gradient

def linearRegression(x, y, alpha, iterations):
    # Init theta
    theta = numpy.zeros((2,1))

    # Make the first column a column on ones in the input
    x = numpy.hstack((numpy.ones((x.shape[0],1)),x))

    # Init an empty list to store them losses
    losses = []

    for i in range(iterations):
        # Calculate loss
        loss = getLoss(x, y, theta)
        losses.append(loss)

        # Calculate Gradient
        gradient = getLinearGradient(x, y, theta)

        # Update the values for theta
        theta -= alpha * gradient

    return {
            'losses': losses,
            'theta': theta
            }

def main():

    # Input
    x = numpy.arange(0,100,1).reshape(-1,1)

    # Output
    y = 10 * x + 10

    # Add random errors to the output
    randomErrors = stats.norm.rvs(size=x.shape, scale=50, random_state=13)
    y = y + randomErrors

    learning_rate = 0.0001
    number_of_iterations = 200

    output = linearRegression(x,y, learning_rate, number_of_iterations)

    losses = output.get('losses', [])
    theta = output.get('theta', [])

    print("The first value for loss:", losses[0])
    print("The final value for loss:", losses[-1], end="\n\n")

    print("The optimal theta:", theta, sep="\n")

if __name__ == "__main__":
    main()
