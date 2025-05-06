#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW03_1
# 229223 Sec 001

import math

def main():
    test_fabric_excess()
    # input
    x = float(input("inches = "))
    # call-in function
    fabric_yards(x)
    # output [inches => yards]
    print(fabric_excess(x))

# Call-in Function
def fabric_yards(inches) :
    yd = math.ceil(inches/36)
    return yd

def fabric_excess(inches):
    inch = 36 - fabric_yards(inches)
    return inch

def test_fabric_excess():
    epsilon = 0.001
    assert math.isclose(fabric_excess(1), 35.0, abs_tol=epsilon)
    assert math.isclose(fabric_excess(10), 35.0, abs_tol=epsilon)
    assert math.isclose(fabric_excess(38), 34.0, abs_tol=epsilon)
    assert math.isclose(fabric_excess(50), 34.0, abs_tol=epsilon)
    assert math.isclose(fabric_excess(100), 33.0, abs_tol=epsilon)
    assert math.isclose(fabric_excess(120), 32.0, abs_tol=epsilon)
    print("All OK!")

if __name__ == '__main__':
    main()