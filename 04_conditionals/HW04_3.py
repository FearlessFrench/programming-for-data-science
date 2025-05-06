#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW04_3
# 229223 Sec 001

def main():
    test_Boolean_is_overlapped()
    # input
    left1 = int(input("l1 = "))
    top1 = int(input("t1 = "))
    width1 = str(input("w1 = "))
    height1 = int(input("h1 = "))
    left2 = int(input("l2 = "))
    top2 = int(input("t2 = "))
    width2 = str(input("w2 = "))
    height2 = int(input("h2 = "))

    # Function
    Boolean_is_overlapped(left1, top1, width1, height1, left2, top2, width2, height2)


def Boolean_is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    if l1 + w1 - l2 < 0:
        print("False")
    else:
        print("true")
    area1 = (l1+w1)*(t1+h1)
    area2 = (l2+w2)*(t2+h2)
    # WTF

def test_Boolean_is_overlapped():
    assert Boolean_is_overlapped(10, 10, 50, 75, 30, 55, 60, 60) == True
    assert Boolean_is_overlapped(10, 10, 50, 75, 70, 55, 60, 60) == False
    print("Gotcha!")

if __name__ == '__main__':
    main()