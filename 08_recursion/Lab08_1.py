#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# Lab08_1
# 229223 Sec 001

def main():
    test_gcd()
    # input
    x = int(input("x = ")) 
    y = int(input("y = "))
    # output
    print(gcd(x, y)) # 1

# gcd = x % y   = z
#     = y % z  = z1
#     = z % z1 = z2
#     .
#     .
#     .
def gcd(x, y):
    # Base case
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def test_gcd():
    assert gcd(19, 71) == 1
    assert gcd(-39, 78) == 39
    print("A Good Start")

if __name__ == "__main__":
    main()