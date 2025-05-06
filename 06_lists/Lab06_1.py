#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# Lab06_1
# 229223 Sec 001
# 30/100
def main():
    # input (n>=3)
    x = str(input())
    # output
    print(triangle(x))


def triangle(n):

    # n = 4
    # \n = 3
    # dot = Row n-2 == 4-2 = 2
    # Row 1   *.*
    # Row 2   *...*
    n = int(n)
    a = "*"

    row1 = (a + "."*1 + a)
    row2 = (a + "."*3 + a)
    row3 = (a + "."*5 + a)
    row4 = (a + "."*7 + a)
    row5 = (a + "."*9 + a)
    row6 = (a + "."*11 + a)
    row7 = (a + "."*13 + a)
    row8 = (a + "."*15 + a)
    row9 = (a + "."*17 + a)
    row10 = (a + "."*19 + a)
    row11 = (a + "."*21 + a)
    row12 = (a + "."*23 + a)

    m1 = "\n" + row1
    m2 = "\n" + row1 + "\n" + row2
    m3 = "\n" + row1 + "\n" + row2 + "\n" + row3
    m4 = "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4
    m5 = "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5
    m6 = "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6
    m7 = "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7
    m8 = "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8
    m9 = "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8 + "\n" + row9
    m10 = "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8 + "\n" + row9 + "\n" + row10
    m11 = "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8 + "\n" + row9 + "\n" + row10 + "\n" + row11
    m12 = "\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4  + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8 + "\n" + row9 + "\n" + row10 + "\n" + row11 + "\n" + row12

    b = "\n" + "* " * n

    if n == 3:
        return a + m1 + b
    elif n == 4:
        return a + m2 + b
    elif n == 5:
        return a + m3 + b
    elif n == 6:
        return a + m4 + b
    elif n == 7:
        return a + m5 + b
    elif n == 8:
        return a + m6 + b
    elif n == 9:
        return a + m7 + b
    elif n == 10:
        return a + m8 + b
    elif n == 11:
        return a + m9 + b
    elif n == 12:
        return a + m10 + b
    elif n == 13:
        return a + m11 + b
    elif n == 14:
        return a + m12 + b
    

def test_triangle():
    T3 = '''*
*.*
* * *
'''
    T7 = '''*
*.* 
*...*
*.....*
*.......*
*.........*
* * * * * * *
'''

    assert triangle(3) == T3
    assert triangle(7) == T7
    print("OK")

if __name__ == '__main__':
    main()