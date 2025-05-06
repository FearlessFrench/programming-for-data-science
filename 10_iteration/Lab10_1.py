#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab10_1
# 229223 Sec 001

import math

def main():
    test_bean_count()
    x = int(input())
    print(bean_count(x))

def bean_count(n):
    if n < 1 or n == 100:
        return 0
    elif n > 100:
        n -= 100
        x = (n//10)
        count = x * 9
        consume = (n//10) * 5
        result = count - consume
        return result
    else:
        x = (n//10) # 9
        count = x * 9  # 81
        consume = (n//10) * 5
        result = count - consume
        return result

def test_bean_count():
    assert bean_count(-1) == 0
    assert bean_count(90) == 36
    print("ok!")
            
if __name__ == "__main__":
    main()