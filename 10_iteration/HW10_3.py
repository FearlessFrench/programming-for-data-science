#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW10_3
# 229223 Sec 001

def main():
    p1 = [(2, 6), (1, 34), (0, -8)]
    # p1 = 𝟔𝒙**2 + 𝟑𝟒x**1 − 𝟖x**0
    p2 = [(2, -6), (0, 2), (1, 1)]
    # p2 = -𝟔𝒙**2 + 2x**0 − 1x**1
    print(polynomial_addition(p1, p2))
    # p1 + p2 = 35x - 6
    #         = 35x**1 - 6x**0
    #         [(1, 35), (0, -6)]

def polynomial_addition(p1, p2):
    while True:
        p3 = p1[0] + p2[0]
        p4 = p1[1] + p2[1]
        p5 = p1[2] + p2[2]
        return p3 + p4 + p5



if __name__ == "__main__":
    main()