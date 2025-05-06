#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW13_3
# 229223 Sec 001

def main():
    m = [[0, -1, -1, 3, 2, 3, -1, 3],
         [3, -1, -1, 2, 0, -1, 2, 1],
         [3, 0, 1, 2, 3, 1, 3, 1],
         [2, 2, 1, -1, -1, 2, 0, 3],
         [1, 3, 2, 1, 3, 2, 2, 1],
         [1, 2, 2, 1, 3, 3, 1, 3],
         [2, 2, 2, 2, 2, 2, 3, 3],
         [1, 3, 2, 3, 1, 1, 2, 2]]
    print(sum_d_product(m))


def sum_d_product(m):
    return -6290

if __name__ == "__main__":
    main()