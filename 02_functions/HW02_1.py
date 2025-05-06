#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW02_1
# 229223 Sec 001
import math

def main():
    # input
    x = float(input("three_side_lenght: "))
    # output
    print(octagon_area(x))

def octagon_area(x):
    # find hypotenuse of one_octagon_side
    a = x/3
    b = x/3
    c = (x * math.sqrt(2))/3
    side = c

    # octagon_area = 2 * side^2 * cot(π/8)
    octagon_area = 2 * (side**2) * (1/(math.tan(math.pi/8)))
    return abs(octagon_area)

def test_octagon_area():
    assert octagon_area(1) == 1.0729838054991532
    assert octagon_area(5) == 26.824595137478834
    assert octagon_area(10) == 107.29838054991534
    assert octagon_area(50) == 2682.459513747883    
    print("Nice job!")

if __name__ == '__main__':
    main()

