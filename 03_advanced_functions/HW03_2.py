#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW03_2
# 229223 Sec 001

import math


def main():
    test_t_area_by_coord()
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    print(t_area_by_coord(a, b, c, d, e, f))

# implement ฟังก์ชันนี้ให้ถูกต้อง
def t_area_by_coord(x1, y1, x2, y2, x3, y3):
    # find side a, b, c using Pythagorean theorem
    a = (((x1-x2)**2 + (y1-y2)**2)**0.5)
    b = (((x1-x3)**2 + (y1-y3)**2)**0.5)
    c = (((x2-x3)**2 + (y2-y3)**2)**0.5)
    # Heron's formula
    s = ((a+b+c)/2)
    area = math.ceil((s*(s-a)*(s-b)*(s-c))**0.5)
    return area


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
# สังเกตวิธีการเขียน test case กรณี output เป็นจำนวนจริง
def test_t_area_by_coord():
    eps = 0.001
    assert math.isclose(t_area_by_coord(2, 0, 0, 0, 0, 2), 2.0, abs_tol=eps)
    assert math.isclose(t_area_by_coord(-1, 0, 0, 1, 1, 0), 1.0, abs_tol=eps)
    assert math.isclose(t_area_by_coord(5, 0, 0, 0, 0, 5), 13.0, abs_tol=eps)
    assert math.isclose(t_area_by_coord(-2, 0, 0, 5, 6, 0), 21.0, abs_tol=eps)

    print("All OK!")


if __name__ == '__main__':
    main()
