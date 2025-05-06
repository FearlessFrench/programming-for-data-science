#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW12_1
# 229223 Sec 001

def main():
    n = 16
    print(nth_term(n))

def nth_term(n):
    if n == 1:
        return 6
    if n == 2:
        return 7
    for i in range(n):
        for j in range(n-1):
            return 6
        for k in range(n+1):
            return 7


if __name__ == "__main__":
    main()