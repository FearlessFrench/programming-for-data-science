#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW03_3
# 229223 Sec 001
import math

def main():
    test_nearest_odd()
    num = float(input())
    print(nearest_odd(num))

# implement ฟังก์ชันนี้ให้ถูกต้อง
def nearest_odd(x):
    m = math.ceil(x/2)
    odd = 2*m - 1
    return odd


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_nearest_odd():
    assert nearest_odd(3) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    print("All OK!")


if __name__ == '__main__':
    main()