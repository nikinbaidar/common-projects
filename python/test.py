#!/usr/bin/env python

x = [0, 10, 'a']

try:
  r =1/x
except ZeroDivisionError:
  r = -1
except TypeError:
  r = -2

print(r)
