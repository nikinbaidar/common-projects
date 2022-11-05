#! /usr/bin/python 

import numpy as np

labels =  {
    'glioma_tumor'    : 0,
    'meningioma_tumor': 1,
    'no_tumor'        : 2,
    'pituitary_tumor' : 3
}

# for label in labels.keys():
#     print(label)

# y = [item for item in range(len(labels.keys()))]

# print(y)

# x = list(np.ones_like(y, dtype=np.int8) * 2)

# print(x)

urls =  {
    ['a', 'b'] : 0,
    ['c', 'd'] : 1,
}

print(urls)
