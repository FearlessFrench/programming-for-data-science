#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW12_3
# 229223 Sec 001

import statistics

def main():
    set_a = {1, 2, 3}
    print(subset_sum(set_a))


def subset_sum(set_a):
    set = set_a.copy() # {1, 2, 3}
    a = set.pop() # 1 
    b = set.pop() # 2
    c = set.pop() # 3
    #print(a)
    #print(b)
    #print(c)
    empty = [0]
    i = [a]
    j = [b]
    k = [c]
    l = [a + b]
    m = [a + c]
    n = [b + c]
    o = [a + b + c]
    list_a = empty+i+j+k+l+m+n+o
    return list_a


if __name__ == "__main__":
    main()