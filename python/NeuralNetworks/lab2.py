#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot
from os import system

def sigmoid(arg):
    ''' This is just a basic sigmoid function.
    Returns the probability that y=1, the shape of the matrix that is returned
    will be same as that of y.
    '''
    return 1 / (1 + np.exp(-arg))

def getPrediction(sigmoidProbability):
    # Use list comprehension to predict the class
    prediction = [ float(probability >= 0.50)
            for probability in sigmoidProbability ]
    # Reshape the prediction to fit the output matrix shape
    prediction = np.array(prediction).reshape(-1,1)
    return prediction

def getCrossEntropyLoss(y, sigmoidX):
    return np.mean(-y * np.log(sigmoidProbability) -
        (1-y) * np.log(1 - sigmoidProbability))

def getCrossEntropyLossGradient(X, y, sigmoidProbability):
    ''' Derivative of the cross loss function.  '''
    numberOfExamples = X.shape[0]
    delta = sigmoidProbability - y
    gradient = (1 / numberOfExamples) * np.dot(X.T, delta)
    return gradient

def performLogisticRegression(X, y, alpha, iterations):

    numberOfExamples = X.shape[0]
    numberOfFeatures = X.shape[1]

    # Initialize theta!
    theta = np.zeros((numberOfFeatures + 1, 1))

    # Add bias to the training set (inputs)
    bias = np.ones((numberOfExamples, 1))
    X = np.hstack((bias,X))

    # Init an empty list to save the loss history
    losses = []

    # START ----------------------

    for current_iteration in range(iterations):

        # Get the probability of y being 1
        sigmoidProbability = sigmoid(X.dot(theta))

        # Calculate (cross-entropy) loss
        loss = getCrossEntropyLoss(y, sigmoidProbability)
        losses.append(loss)

        # Calculate Gradient
        gradient = getCrossEntropyLossGradient(X, y, sigmoidProbability)

        # Update the values for theta
        theta -= alpha * gradient

        # To test for convergence
        if losses[-1] < 0.01:
            print(f"Model converges after {current_iteration} iterations")
            break

    # END --------------------------

    return {
      'losses': losses,
      'theta': theta,
      'actualIterations': current_iteration,
    }

def plotLosses(losses):
    pyplot.plot(np.arange(len(losses)), losses, label='losses')
    pyplot.xlabel("Iterations")
    pyplot.ylabel("Cross Entropy Loss")
    pyplot.axhline(0.0, ls= '-.', color='black')
    pyplot.title("Title: Training Losses")
    pyplot.legend()
    pyplot.show()

def plotDecisionBoundary(X, y, theta):
  ''' Plot decision boundary..
  '''
  xDelta = 0.1
  xx = np.arange(0, 1+xDelta, xDelta)
  yy = (-1*theta[0,0] - theta[1,0]*xx)/theta[2,0]
  pyplot.plot(xx, yy, color='black', label="Fitted Decision Boundary")

  for yVal in np.unique(y):
    yIndex = y.reshape(-1) == yVal
    x1 = X[yIndex, 0]
    x2 = X[yIndex, 1]
    pyplot.scatter(x1, x2, marker='x', s=100, label=f"y=={yVal}")

  pyplot.xlabel("X1")
  pyplot.ylabel("X2")
  pyplot.grid()
  pyplot.xlim(0, 1)
  pyplot.ylim(0, 1)
  pyplot.title("Input datapoints vs. output labels")
  pyplot.legend()
  pyplot.show()

# main:

system("clear")

X = np.array([
  [0.15, 0.8 ],
  [0.22, 0.75],
  [0.43, 0.44],
  [0.61, 0.25],
  [0.7 , 0.15],
  [0.88, 0.02],
  [0.25, 0.4 ],
  [0.3 , 0.85],
  [0.37, 0.75],
  [0.51, 0.7 ],
  [0.7 , 0.41],
  [0.82, 0.21],
  [0.61, 0.61],
  [0.78, 0.61]
])

y = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]).reshape(-1,1)

output = performLogisticRegression(X, y, 2.7182, 25000)

losses = output['losses']

if len(losses) > 0:
  print (f"Final loss value: {losses[-1]:.4f}, which is below our"\
          f"threshold?: {losses[-1] <= 0.01}\n")

plotLosses(losses)

finalTheta = output['theta']

print(f"The final theta is:\n {finalTheta}")

plotDecisionBoundary(X, y, finalTheta)

def checkEqual(X, y, theta):
  ''' Problem 8: Check if all values of y predicted equals actual y.
      :param X: Real intputs (#datapoints, #features)
      :param y: Real output (#datapoints, 1)
      :param theta: parameters (#features+1, 1)
      :returns: Boolean True if all y_predicted equals y_true! else False
  '''
  bias = np.ones((X.shape[0], 1))
  X = np.hstack((bias,X))
  sigmoidProbability = sigmoid(X.dot(theta))
  y_predicted = getPrediction(sigmoidProbability)
  return all(y_predicted == y)

if checkEqual(X, y, finalTheta):
    print("The predication matches the output!")
