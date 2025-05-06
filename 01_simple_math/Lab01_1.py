#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# Lab01_1
# 229223 Sec 001

# Use Heron (of Alexandria) Formula
# 3 input, data type: integer
# 1 output, data type: integer

import math

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
s = ((a+b+c)/2)
area = math.ceil((s*(s-a)*(s-b)*(s-c))**0.5)
print(area)
