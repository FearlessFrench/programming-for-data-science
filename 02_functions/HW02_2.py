#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW02_2
# 229223 Sec 001
import math

def main():
    # input
    x = int(input())
    y = int(input())
    # output
    print(kth_digit(x, y))

def kth_digit(number, k):
    k >= 0
    # num4 = number // 1000 % 10
    # num3 = number // 100 % 10
    # num2 = number // 10 % 10
    # num1 = number // 1 % 10
    number = number // (10**k) % 10
    return number

if __name__ == '__main__':
    main()
