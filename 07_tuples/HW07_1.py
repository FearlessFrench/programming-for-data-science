#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW07_1
# 229223 Sec 001

def main():
    # input (number >= 3)
    number = 3
    a = str(input())
    sep = " "
    # output
    print(square_frame(number, sep.join(a)))


def square_frame(n, sep=' '):
    if n < 3:
        return None
    else:
        n *= n
        stg = list(map(str, range(n)))

        print(stg)
        if stg[-1] >= 10:
            return # zero padding
        return stg[1:4] +'\n'+ stg[-1] +" "+ stg[4] +'\n'+ stg[-2] + stg[-3] + stg[-4]


def test_num_to_word():
    print

if __name__ == '__main__':
    main()