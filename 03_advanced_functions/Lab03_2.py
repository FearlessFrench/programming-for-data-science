#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab03_2
# 229223 Sec 001
import math

def main() :
    test_fabric_yards()
    # input
    x = int(input())
    # output [inches => yards]
    print(fabric_yards(x))

def fabric_yards(inches) :
    # inches to yards ==> 1 yd = 36 inch ==> [inches/36 = yards] or [yards x 36 = inches]
    # เราจะต้องซื้อเป็นหน่วยจำนวนเต็มเท่านั้น เช่น หากต้องการใช้แค่ 1 นิ้ว ก็จะต้องซื้อทั้งหลา 
    yd = math.ceil(inches/36)
    return yd

def test_fabric_yards() :
    assert fabric_yards(1) == 1
    assert fabric_yards(2) == 1
    assert fabric_yards(3) == 1
    assert fabric_yards(4) == 1
    assert fabric_yards(5) == 1
    assert fabric_yards(10) == 1
    assert fabric_yards(20) == 1
    assert fabric_yards(30) == 1
    assert fabric_yards(38) == 2
    assert fabric_yards(40) == 2
    assert fabric_yards(50) == 2
    assert fabric_yards(100) == 3
    assert fabric_yards(120) == 4
    assert fabric_yards(150) == 5
    assert fabric_yards(180) == 5
    assert fabric_yards(200) == 6
    assert fabric_yards(250) == 7
    assert fabric_yards(275) == 8
    assert fabric_yards(300) == 9
    assert fabric_yards(380) == 11
    print("Pass!")

if __name__ == '__main__' :
    main()
