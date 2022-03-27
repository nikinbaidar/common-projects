#!/usr/bin/env python

import numpy

from sklearn.preprocessing import MinMaxScaler

def MyScaler(array):
  length  = len(array)
  minimum = min(array)
  maximum = max(array) 

  array = [ (item - minimum)/maximum for item in array ]
  array[array.index(max(array))] = 1.0

  return array

numbers = [1, 2, 3, 4]

print(MyScaler(numbers))

numbers = numpy.array(numbers).reshape(-1,1)
scaler = MinMaxScaler()
scaled_array = scaler.fit_transform(numbers)

print(scaled_array)
