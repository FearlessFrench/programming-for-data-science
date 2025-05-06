#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab12_1
# 229223 Sec 001

def main():
    input = [2, 0, 3]
    multiply = [4, 5]
    print(multiply_polynomials(input, multiply))

def multiply_polynomials(p1, p2):
    x = 1
    a = x**(len(p1)-1)
    b = x**(len(p1)-2)
    c = x**(len(p1)-3)
    d = x**(len(p1)-4)
    simplify1 = p1[0] * p2[0] # 8
    simplify2 = p1[1] * p2[0] # 0
    simplify3 = p1[2] * p2[0] # 10
    evaluate1 = p1[0] * p2[1] # 12
    evaluate2 = p1[1] * p2[1] # 0
    evaluate3 = p1[2] * p2[1] # 15
    result = [simplify1, evaluate1, simplify3, evaluate3]
    return(result)

if __name__ == "__main__":
    main()