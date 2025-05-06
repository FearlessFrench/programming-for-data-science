#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW04_2
# 229223 Sec 001


def main():

    a = input() # input = 1 2 3 4 >> list of str

    b = int(input())
    # -4,0 >>>  1 2 3 4

    #  -3  >>>  4 1 2 3 \
    #  -2  >>>  3 4 1 2  |-> (-1, -2, -3)
    #  -1  >>>  2 3 4 1 /

    #   0  >>>  1 2 3 4

    #   1  >>>  4 1 2 3 \
    #   2  >>>  3 4 1 2  |-> (1, 2, 3)
    #   3  >>>  2 3 4 1 /

    #  0,4 >>>  1 2 3 4

    # IF b = 105 then b = 105 % 4 = 1
    # In Conclusion: b = b % 4

    # output
    print(dest_rotate_list(a, b))


def dest_rotate_list(list_a, n):  # หมุน list_a ไปขวา n ตำแหน่ง (หรือ ไปซ้าย -n)
    # Using Tuple Swap

    # Turn String to Integer >>> list_a = [1, 2, 3, 4]
    list_a = list_a.split()
    # list_a = ['1', '2', '3', '4']
    if n > 0:
        n = n % 4
        if n == 0:
            return list(map(int, list_a))
        elif n == 1:
            # [1, 2, 3, 4] = [4, 1, 2, 3]
            list_a[0], list_a[1], list_a[2], list_a[3] = list_a[3], list_a[0], list_a[1], list_a[2]
            list_a = list(map(int, list_a))
            return list_a 
        elif n == 2:
            # [1, 2, 3, 4] = [3, 4, 1, 2]
            list_a[0], list_a[1], list_a[2], list_a[3] = list_a[2], list_a[3], list_a[0], list_a[1]
            list_a = list(map(int, list_a))
            return list_a
        elif n == 3:
            # [1, 2, 3, 4] = [2, 3, 4, 1]
            list_a[0], list_a[1], list_a[2], list_a[3] = list_a[1], list_a[2], list_a[3], list_a[0]
            list_a = list(map(int, list_a))
            return list_a
    elif n < 0:
        n = n % -4
        if n == 0:
            return list(map(int, list_a))
        elif n == -1:
            # [1, 2, 3, 4] = [2, 3, 4, 1]
            list_a[0], list_a[1], list_a[2], list_a[3] = list_a[1], list_a[2], list_a[3], list_a[0]
            list_a = list(map(int, list_a))
            return list_a
        elif n == -2:
            # [1, 2, 3, 4] = [3, 4, 1, 2]
            list_a[0], list_a[1], list_a[2], list_a[3] = list_a[2], list_a[3], list_a[0], list_a[1]
            list_a = list(map(int, list_a))
            return list_a
        elif n == -3:
            # [1, 2, 3, 4] = [4, 1, 2, 3]
            list_a[0], list_a[1], list_a[2], list_a[3] = list_a[3], list_a[0], list_a[1], list_a[2]
            list_a = list(map(int, list_a))
            return list_a
    else:
        return list_a # [1, 2, 3, 4]


if __name__ == '__main__':
    main()
