#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW07_2
# 229223 Sec 001

def main():
    # input (LISTA >= 0)int(input())
    LISTA = [9, 8, 7, 6, 5, 4, 3, 2]
    # output
    print(medal_allocation(LISTA))


def medal_allocation(list_a):   1

    no_medal = [] # Empty list
    # sorting the list
    list_a = list_a.sort()
    # [2, 3, 4, 5, 6, 7, 8, 9]
    a = list_a[-1]
    b = list_a[-2]
    c = list_a[-3]
    d = list_a[-4]
    e = list_a[-5]
    zero = list_a[0]
    if zero * a == []:
        return no_medal
    elif a > b:
        gold = [a]
        silver = [b]
        if b > c:
            bronze = [c]
            if c == d:
                bronze = [c, d]
                return ([gold],[silver],[bronze])
            return ([gold],[silver],[bronze])
        else:
            silver = [b, c]
            return ([gold],[silver],[bronze])
    elif a == b:
        gold = [a, b]
        silver = no_medal
        if c == d:
            if c < b:
                bronze = [c, d]
                return ([gold],[silver],[bronze])
            elif c == b:
                gold = [a, b, c, d]
                bronze = no_medal
                return ([gold],[silver],[bronze])
        bronze = [c]
        return ([gold],[silver],[bronze])


if __name__ == '__main__':
    main()