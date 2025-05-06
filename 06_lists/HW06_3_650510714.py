#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW04_3
# 229223 Sec 001
# 38/100
def main():
    # input: 1 2 3 4 5
    x = map(int, input().split())
    # [1, 2, 3, 4, 5] >>> list of Integer
    list_x = list(x)
    window_size = int(input()) # 3
    # output
    print(moving_average(list_x, window_size))


def moving_average(list_a, w):
    if w == 2:
        a = sum(list_a[0:2]) / w
        b = sum(list_a[0+1:2+1]) / w
        c = sum(list_a[0+2:2+2]) / w
        d = sum(list_a[0+3:2+3]) / w
        list_b = [a, b, c, d]
        return list_b
    elif w == 3:
        a = sum(list_a[0:3]) / w
        b = sum(list_a[0+1:3+1]) / w
        c = sum(list_a[0+2:3+2]) / w
        list_b = [a, b, c]
        return list_b


if __name__ == '__main__':
    main()
