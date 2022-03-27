#!/usr/bin/env python

def gcd(num1,num2):
    if num1 == num2 == 0:
        raise ValueError
    elif num1 < num2:
        num1, num2 = num2, num1
    while (num1 % num2 !=0):
        num3 = num2
        num2 = num1 % num3
        num1 = num3
    return num2

print(gcd(7,14));
