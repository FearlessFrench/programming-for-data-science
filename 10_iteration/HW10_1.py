#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW10_1
# 229223 Sec 001

import math

def main():
    x = int(input())
    b = int(input())
    print(float_to_base_b(x, b))

def decimal_to_binary(num, times) :
    binary = ""
    # to integral
    integral = int(num)
    # to fraction
    fraction = num - integral
    # integral to binary
    while integral:
        a = integral % 2
        # Append 0 in binary
        binary += str(a);
        integral //= 2
    # reverse the string to get the binary numbers
    binary = binary[ : : -1]
    # append point for fraction
    binary += '.'
    # fraction to binary
    while times: # = 6
        # find binary of fraction formula
        fraction *= 2
        # fraction to binary
        finary = int(fraction)
        if finary == 1: 
            fraction -= finary # fraction - 1
            binary += '1' 
        else :
            binary += '0'
        times -= 1
    return binary


def decimal_to_ternary(num):
    quotient = num / 3
    remainder = num % 3
    if quotient == 0:
        return ""
    else:
        return decimal_to_ternary(int(quotient)) + str(int(remainder))


def decimal_to_octal(num):
    octal = []
    while num > 0:
        r = num % 8
        octal.append(r)
        num = num // 8
    for i in reversed(octal):
        print(i, end="")


def decimal_to_hexadecimal(num):
    first_v = str(num)[0]
    decimal = int(num)
    if first_v == '-': 
        hex_dec = hex(decimal)[3:]
    else:
        hex_dec = hex(decimal)[2:]
    return hex_dec


def float_to_base_b(x, b):
    if b == 2:
        return decimal_to_binary(x, 6)
    if b == 3:
        return decimal_to_ternary(x)
    if b == 8:
        return decimal_to_octal(x)
    if b == 16:
        return decimal_to_hexadecimal(x)
            



if __name__ == "__main__":
    main()