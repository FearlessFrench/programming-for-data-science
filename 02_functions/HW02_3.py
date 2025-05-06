#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW02_3
# 229223 Sec 001
import math
#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW02_2
# 229223 Sec 001

def main():
    # input
    x = int(input())
    y = int(input())
    z = int(input())
    # output
    print(set_kth_digit(x, y, z))

def kth_digit(number, k):
    num = number // (10**k) % 10
    return num

def set_kth_digit(number, k, value): # number = 678'9' , k = 0 , value = 5 ==> 678'5'
    n = kth_digit(number, k)           # ใช้ฟังก์ชัน = 8
    result = number - (n - value) * (10**k)  # 6789-(8-5)*10 = 6785
    return result # 6785


if __name__ == '__main__':
    main()
