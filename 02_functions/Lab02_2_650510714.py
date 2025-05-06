#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab02_1
# 229223 Sec 001

def main():
    # input
    x = int(input())
    # output
    print(reverse_digits(x))

# implement ฟังก์ชันนี้ให้ถูกต้อง
def reverse_digits(x):          # x = 1
    rev1 = 0
    rev1 = rev1 * 10 + (x % 10)   # 0*10 + 1%10 = 1
    x1 = x // 10                 # 1//10 = 0

    rev2 = rev1 * 10 + (x1 % 10)   # 1*10 + 0%10 = 10 + 0 = 10
    x2 = x1 // 10                 # 0//10 = 0

    rev3 = rev2 * 10 + (x2 % 10)   # 10*10 + 0%10 = 100 + 0 = 100
    x3 = x2 // 10                 # 0//10 = 0

    rev4 = rev3 * 10 + (x3 % 10)   # 100*10 + 0%10 = 1000 + 0 = 1000
    return abs(rev4)

# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_reverse_digits():
    assert reverse_digits(1234) == 4321
    assert reverse_digits(1) == 1000
    assert reverse_digits(5) == 5000
    assert reverse_digits(6789) == 9876  
    print("All OK!")


if __name__ == '__main__':
    main()
