#!/usr/bin/env python

from sklearn.linear_model import LogisticRegression
from scipy.sparse import csr_matrix, csc_matrix

import numpy

"""
The LogisticRegression class implements regularized logistic regression variety
of solvers; see solver-penalty compatibility. For optimal performance use CSR
matrices containing 64-bit floats.
"""

def train (x,y):
  model = LogisticRegression(solver='saga', penalty='elasticnet', l1_ratio=0.2)
  fitted = model.fit(x,y)
  return fitted

x = numpy.array([
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

y = numpy.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], dtype=numpy.float64)

x = csr_matrix(x, dtype=numpy.float64).toarray()
y = csr_matrix(y).toarray()
y = numpy.ravel(y)

model = train(x,y)

x_new = [[0.79, 0.70]]
y_new = model.predict(x_new)
print(y_new[0])
