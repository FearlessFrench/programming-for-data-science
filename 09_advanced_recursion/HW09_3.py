#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW09_3
# 229223 Sec 001

from statistics import mode

def main():
    test_left_max()
    # input
    x = [3, 3, 1, 1, 2, 4]
    # output
    print(left_max(x))


def left_max(n):
    if n < 0:
        return None
    else:
        return left_max(n)

def test_left_max():
    assert left_max([2, 8, 1]) == [2, 8, 8]
    assert left_max([3, 3, 1, 1, 2, 4]) == [3, 3, 3, 3, 3, 4]
    print("Simulation Completed")


if __name__ == "__main__":
    main()