#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW01_1
# 229223 Sec 001

# y = (mx + b) , m = (slope) , b = (intersected point on y-axis)
# y = (m1*x + b1) = (m2*x + b2)

m1 = float(input("m1: "))
b1 = float(input("b1: "))
m2 = float(input("m2: "))
b2 = float(input("b2: "))
m1 != m2
# y1 = (m1*x + b1)
# y2 = (m2*x + b2)
#          y1 = y2
# (m1*x + b1) = (m2*x + b2)
#      (m3*x) = b2 - b1
#           x = (b2 - b1)/(m3)
x = (b2 - b1)/(m1-m2)
# replacing x
y = (m1*x + b1) and (m2*x + b2)

print("Lines intersect at",(x,y))