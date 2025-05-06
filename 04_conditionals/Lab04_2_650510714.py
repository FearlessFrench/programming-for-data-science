#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab04_2
# 229223 Sec 001

# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function is_p_triple()

def main():
    test_p_triple()
    # input
    a = int(input())
    b = int(input())
    c = int(input())
    # output
    print(is_p_triple(a, b, c))

def is_p_triple(x, y, z):
    if   x == y:
        return(False)
    elif y == z:
        return(False)
    elif abs(x - y) > 10:
        return(False)
    elif abs(y - z) > 10:
        return(False)
    else:
        return(True)

def test_p_triple():
    assert is_p_triple(4, 5, 3) == True
    assert is_p_triple(42, 9, 41) == False
    assert is_p_triple(5, 12, 13) == True
    assert is_p_triple(1, 1, 2) == False
    print("all ok!")


if __name__ == '__main__':
    main()