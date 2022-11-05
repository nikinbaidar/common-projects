#!/usr/bin/env python
# WAP to input a number, if it is not a number then generate an error message

import numpy as np

x = np.zeros(3)


x = [4, 0, 65, 'a']

for item in x:
  try:
    r = 1/item
  except ZeroDivisionError:
    print(ZeroDivisionError)
  except TypeError:
    print(TypeError)
  else:
    print(r)

# print()
# raise MemoryError("Nikin Baidar")
