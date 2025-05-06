#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW05_2
# 229223 Sec 001

def main():
    # input
    number = str(input())
    position = str(input())
    # output
    print(rotate(number, position))


def rotate(num, pos):
    # pos[0] == pos[-5] == pos[5+0] == pos[10] == ... unit = 0, 5, -5, -10
    # pos[1] == pos[-4] == pos[5+1] == pos[11] == ... unit = 1, 6, -4, -9
    # pos[2] == pos[-3] == pos[5+2] == pos[12] == ... unit = 2, 7, -3, -8
    # pos[3] == pos[-2] == pos[5+3] == pos[13] == ... unit = 3, 8, -2, -7
    # pos[4] == pos[-1] == pos[5+4] == pos[14] == ... unit = 4, 9, -1, -6
    n = int(num)

        # "12345", "103"
    if int(pos) >= 0:
        p = pos  # "103"
        x = p[-1] # "3"
        unit = int(x)  # 3
        if unit == 0:
            return str(n)
        elif unit == 1:
            a = num[-1] + num[0:4]  # 51234
            return str(a)
        elif unit == 2:
            a = num[-1] + num[0:4]  # 51234
            b = a[-1] + a[0:4]  # 45123
            return str(b) 
        elif unit == 3:
            a = num[-1] + num[0:4]  # 51234
            b = a[-1] + a[0:4]  # 45123            
            c = b[-1] + b[0:4]  # 34512
            return str(c)
        elif unit == 4:
            a = num[-1] + num[0:4]  # 51234
            b = a[-1] + a[0:4]  # 45123            
            c = b[-1] + b[0:4]  # 34512
            d = c[-1] + c[0:4]  # 23451
            return str(d)

        elif unit == 5:
            return str(n)
        elif unit == 6:
            a = num[-1] + num[0:4]  # 51234
            return str(a)
        elif unit == 7:
            a = num[-1] + num[0:4]  # 51234
            b = a[-1] + a[0:4]  # 45123
            return str(b)
        elif unit == 8:
            a = num[-1] + num[0:4]  # 51234
            b = a[-1] + a[0:4]  # 45123            
            c = b[-1] + b[0:4]  # 34512
            return str(c)
        elif unit == 9:
            a = num[-1] + num[0:4]  # 51234
            b = a[-1] + a[0:4]  # 45123            
            c = b[-1] + b[0:4]  # 34512
            d = c[-1] + c[0:4]  # 23451
            return str(d)

        
    if int(pos) <= 0:
        p = pos  # "-103"
        x = p[-1] # "3"
        unit = int(x)  # 3
        unit *= -1  # -3
        if unit == 0:
            return str(n)
        elif unit == -1:
            a = num[1:] + num[0]  # 23451
            return str(a)
        elif unit == -2:
            a = num[1:] + num[0]  # 23451
            b = a[1:] + a[0]  # 34512
            return str(b)
        elif unit == -3:
            a = num[1:] + num[0]  # 23451
            b = a[1:] + a[0]  # 34512            
            c = b[1:] + b[0]  # 45123
            return str(c)
        elif unit == -4:
            a = num[1:] + num[0]  # 23451
            b = a[1:] + a[0]  # 34512            
            c = b[1:] + b[0]  # 45123
            d = c[1:] + c[0]  # 51234
            return str(d)

        elif unit == -5:
            return str(n)
        elif unit == -6:
            a = num[1:] + num[0]  # 23451
            return str(a)
        elif unit == -7:
            a = num[1:] + num[0]  # 23451
            b = a[1:] + a[0]  # 34512
            return str(b)
        elif unit == -8:
            a = num[1:] + num[0]  # 23451
            b = a[1:] + a[0]  # 34512            
            c = b[1:] + b[0]  # 45123
            return str(c)
        elif unit == -9:
            a = num[1:] + num[0]  # 23451
            b = a[1:] + a[0]  # 34512            
            c = b[1:] + b[0]  # 45123
            d = c[1:] + c[0]  # 51234
            return str(d)


def test_rotate():
    assert test_rotate("12345", "3") == "34512"
    assert test_rotate("12345", "2") == "45123"
    assert test_rotate("12345", "-3") == "45123"
    assert test_rotate("12345", "-103") == "45123"
    print("Beautiful Game")


if __name__ == "__main__":
    main()