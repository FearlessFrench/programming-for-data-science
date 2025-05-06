#!/usr/bin/env python3 
# Panutad Sirikul
# 650510714 
# Lab01_1
# 229223 Sec 001

# Problem Analysis
# 3 input, data type: integer
# 1 output, data type: integer

import math

a = 3
b = 4
c = 5
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
x = math.ceil(area)
print("a:", a)
print("b:", b)
print("c:", c)
print("area:", x)


a = 4
b = 13
c = 15
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
x = math.ceil(area)
print("a:", a)
print("b:", b)
print("c:", c)
print("area:", x)