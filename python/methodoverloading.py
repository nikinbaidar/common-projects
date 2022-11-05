#!/usr/bin/env python
# At the backend, dispatcher creates an object which stores different
# implementation and on runtime, it selects the appropriate method as
# the type number of paramters passed.

from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    return a + b

@dispatch(int, int, int)
def add(a, b, c):
    return a + b + c

print(add(1, 3))
print(add(1, 3, 6))

print("-"*30)

# If I define the above function "add" with a different name "sum", then the
# original "sum" function loses it's namespace. Say you want to use the same
# name as the built-in sum, just wrap the dispatches inside a class or maybe a
# different module (afterall method overloading is a concept from OOP).

class MethodOverloading:

    @dispatch(int, int)
    def sum(a, b):
        return a + b

    @dispatch(int, int, int)
    def sum(a, b, c):
        return a + b + c

adder = MethodOverloading()

print(adder.sum(1, 3))
print(adder.sum(1, 3, 6))
print(sum([1, 3, 6]))
