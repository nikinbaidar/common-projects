#!/usr/bin/env python

import numpy

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

categoricalData = numpy.array([['protocol_type'], ['service'], ['flag']])
print(categoricalData)

scaled = OneHotEncoder().fit_transform(categoricalData).toarray()
print(scaled)
