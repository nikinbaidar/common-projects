#!/usr/bin/env python

def gcd(num1, num2):
    if num1 == num2 == 0:
        raise ValueError
    elif num1 < num2:
        num1, num2 = num2, num1
    while (num1 % num2 != 0):
        num3 = num2
        num2 = num1 % num3
        num1 = num3
    return num2

x = (7,14)

print("HCF of ", x , "is",  gcd(x[1], x[0]));

