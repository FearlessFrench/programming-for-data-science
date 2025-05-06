#!/usr/bin/env python3

# Compute the area of a triangle using a Heron's formula\
a = 3
b = 4
c = 5
s = (a+b+c)/2  # 6
area = (s*(s-a)*(s-b)*(s-c))**0.5

print("a =", a)
print("b =", b)
print("c =", c)
print("area =", area)