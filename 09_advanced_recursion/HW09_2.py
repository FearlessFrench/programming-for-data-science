#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW09_2
# 229223 Sec 001

from statistics import mode

def main():
    test_longest_digit_run()
    # input
    x = int(input())
    # output
    print(longest_digit_run(x))


def longest_digit_run(n):
    if n == 0:
        return 0
    else:
        list_mode = list(map(int,str(n))) # [1, 1, 7, 7, 7, 3, 3, 2]
        digits = mode(list_mode) # 7
        return list_mode.count(digits)


def test_longest_digit_run():
    assert longest_digit_run(11777332) == 3
    assert longest_digit_run(1177332) == 2
    print("Simulation Completed")


if __name__ == "__main__":
    main()