#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab03_1
# 229223 Sec 001
import math

def main() :

    x = int(input())

    print(nth_fibonacci_number(x))

def nth_fibonacci_number(n) :
    φ = (1 + math.sqrt(5))/2
    F = math.floor((φ**n)/(math.sqrt(5)) + (1/2))
    return F

def test_fibonacci_number() :
    assert nth_fibonacci_number(0) == 0
    assert nth_fibonacci_number(1) == 1
    assert nth_fibonacci_number(2) == 1
    assert nth_fibonacci_number(3) == 2
    assert nth_fibonacci_number(4) == 3
    assert nth_fibonacci_number(5) == 5
    assert nth_fibonacci_number(6) == 8
    assert nth_fibonacci_number(7) == 13
    assert nth_fibonacci_number(8) == 21
    assert nth_fibonacci_number(9) == 34
    assert nth_fibonacci_number(10) == 55
    assert nth_fibonacci_number(11) == 89
    assert nth_fibonacci_number(12) == 144
    assert nth_fibonacci_number(13) == 233
    assert nth_fibonacci_number(14) == 377
    assert nth_fibonacci_number(15) == 610
    assert nth_fibonacci_number(16) == 987
    assert nth_fibonacci_number(17) == 1597
    assert nth_fibonacci_number(18) == 2584
    assert nth_fibonacci_number(19) == 4181
    print("Pass!!")


if __name__ == '__main__' :
    main()