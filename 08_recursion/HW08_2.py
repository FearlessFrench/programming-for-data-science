#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW08_2
# 229223 Sec 001

def main():
    x = 10
    b = 2
    print(base_b(x, b))

def base_b(x, b):
    if (b < 2) or (b > 10):
        return None
    else:
        return base_b(x//b, b)


if __name__ == "__main__":
    main()