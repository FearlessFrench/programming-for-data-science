#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW01_2
# 229223 Sec 001

# sum(k=1}^(n) = (n*(n+1))/2
# Condition => (0 ≤ x ≤ y)

x = int(input("x: "))
y = int(input("y: "))

n = y - x + 1

sum = (n*(n+1))/2  # Sum of Natural Numbers Formula
sum = (n*(x+y))/2  # Sum of Integers Formula

print("sum is:", sum)
