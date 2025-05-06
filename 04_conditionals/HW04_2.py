#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW04_2
# 229223 Sec 001

def main():
    # input
    h1 = int(input("hour1 = "))
    m1 = int(input("min1 = "))
    p1 = str(input("AM or PM = "))
    h2 = int(input("hour2 = "))
    m2 = int(input("min2 = "))
    p2 = str(input("AM or PM = "))  

    # output
    print(min_diff(h1, m1, p1, h2, m2, p2))


def min_diff(hour1, min1, period1, hour2, min2, period2):

    # calculate hour 00:00-23:59
    if period1 == "PM":
        hour1 = 12 + hour1

    if period2 == "PM":
        hour2 = 12 + hour2

    # now let's find d_min
    hour_to_minute = abs(hour1*60 - hour2*60)
    min_to_minute = abs(min1 - min2)
    return hour_to_minute + min_to_minute


def test_min_diff():
    assert test_min_diff(8, 23, 'AM', 8, 24, 'AM') == 1
    assert test_min_diff(8, 23, 'AM', 1, 24, 'PM') == 301
    assert test_min_diff(1, 24, 'PM', 8, 23, 'AM') == 301
    assert test_min_diff(8, 23, 'AM', 8, 24, 'PM') == 721
    print("It works!")


if __name__ == '__main__':
    main()