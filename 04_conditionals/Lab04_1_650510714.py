#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab04_1
# 229223 Sec 001
import math

# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function circle_intersect()

def main():
    test_circle_intersect()
    x = float(input())
    y = float(input())
    r = float(input())
    a = float(input())
    b = float(input())
    c = float(input())
    ep = float(input("epsilon = "))
    print(circle_intersect(x, y, r, a, b, c, ep))

def circle_intersect(x1, y1, r1, x2, y2, r2, epsilon=10**-6):
    d_xy = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    r = r1 + r2
    result = r - d_xy
    if result < 0:
        return -1
    if epsilon > result:
        return 0
    return result


def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("all ok!")


if __name__ == '__main__':
    main()
