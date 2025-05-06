#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW01_3
# 229223 Sec 001

# When first Two-Digits are >= 50฿ | change it to 98฿ | Remain the hundred digit of a product (371 to 398)
# When first Two-Digits are less than 50฿ | change it to 98฿ | but lowering the hundred digit by 1 (371 to 298)


old = int(input("Old price: ")) # 371

hundred = old // 100 # 3
third_digit = hundred * 100 # 300

import math
a = (old/100)
ten = math.floor((a - hundred) * 10) # 7
unit = old - (hundred*100) - (ten*10) # 1

two_digits = ((a - hundred) * 100) # 71

x = 98 - two_digits # 27
new = old + x
 
print("New price:", new)