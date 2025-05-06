#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW08_1
# 229223 Sec 001

from math import isclose

def main():
    #test_pi()
    n = input()
    print(pi(n))

    # p = n*2
    # pi(5) == pi(4) + 4/(p*(p+1)*(p+2))
def pi(n):
    p = n*2
    if n == 0:
        return 3
    else:
        return 4/(p*(p+1)*(p+2)) + pi(n-1)


def test_pi():
    epsilon = 10**-10
    assert isclose(pi(0), 3, abs_tol=epsilon)
    assert isclose(pi(1), 3.1666666666666665, abs_tol=epsilon)
    assert isclose(pi(2), 3.1333333333333333, abs_tol=epsilon)
    assert isclose(pi(5), 3.1427128427128426, abs_tol=epsilon)
    print("All OK!")


if __name__ == "__main__":
    main()