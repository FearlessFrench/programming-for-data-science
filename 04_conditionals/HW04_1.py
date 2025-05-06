#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW04_1
# 229223 Sec 001

def main():
    # input 3 ตัว ชนิด integer
    x = int(input())
    y = int(input())
    z = int(input())
    # call-in function
    my_min_mid_max(x, y, z)


def my_min_mid_max(a, b, c):
    # find max_ and min_ from a,b,c
    if a > b:
      max_ = a
      min_ = b
    else:
      max_ = b
      min_ = a

    # compare c to min
    if c < min_:
      min_ = c
    # output 1 int
    print("min =", min_)

    # compare c to max
    if c > max_:
      max_ = c
    # output 2 int
    print("max =", max_)    

    # find mid_ from a,b,c
    if max_ - min_ > min_:
      mid_ = min_ + 1
    else:
      mid_ = min_
    # output 3 int
    print("mid =", mid_)


# def test_my_min_mid_max(): หาค่า max ได้กี่วิธี
      # a,b,c ไม่เหมือนกัน
    # assert test_my_min_mid_max(1, 2, 3) == 3! = 6 วิธี
      # เหมือนกัน 2 ตัว และ น้อยกว่า 1 ตัว
    # assert test_my_min_mid_max(2, 2, 1) == 3!/2 = 3 วิธี
      # เหมือนกัน 2 ตัว และ มากกว่า 1 ตัว
    # assert test_my_min_mid_max(2, 2, 3) == 3!/2 = 3 วิธี
      # a,b,c เหมือนกัน
    # assert test_my_min_mid_max(1, 1, 1) == 1 วิธี


if __name__ == '__main__':
    main()