# Importing basic lib
import pandas as pd
import numpy as np


# Import data from your local system
Data = pd.read_excel("./Data.xlsx")

# Cross checking if Data is imported
Data

# Spliting of data as input and output
X = Data.iloc[:, :1].values
y = Data.iloc[:, 1:2].values

# Creating a column of ones and inserting to x
ones = np.ones((97,1))
X = np.insert(X, [0], ones, axis =1)

# Creating initial 2X1 matrix of thetas
theta = np.zeros((2,1))


# Build a function to calculate Cost Function
def costfunction(X, y, theta):
    prediction = np.matmul(X, theta)
    sqerror = np.square(np.subtract(prediction, y))
    sum = np.array(sqerror).sum()
    J = 1/194*sum

    return J


# Build a function to calculate Gradient Descent
def gradientdescent (X, y, alpha, theta):
    # theta = np.zeros((2,1))
    for i in range(1500):
        prediction = np.matmul(X, theta)
        error1 = np.subtract(prediction, y)
        error2 = (np.subtract(prediction, y))*X[:, 1:2]

        sum1 = np.array(error1).sum()
        sum2 = np.array(error2).sum()

        temp0 = theta[0:1, 0:1] - ((alpha/97) * (sum1))
        temp1 = theta[1:2, 0:1] - ((alpha/97) * (sum2))

        theta[0:1, 0:1] = temp0 # Simultaneously updating theta
        theta[1:2, 0:1] = temp1

    return theta


# Check values for CF and GD
CF = costfunction(X, y, np.array([[-9], [3]]))
GD = gradientdescent(X, y, 0.01, theta)

print("Cost Funcation is : \n", CF)
print("\n Theta values are : \n", GD)
