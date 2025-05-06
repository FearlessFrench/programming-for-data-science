#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW12_2
# 229223 Sec 001

import statistics

def main():
    list_a = [28, 14, 13, 21, 19, 27, 23, 30, 16, 3]
    print(median_of_median(list_a))


def median_of_median(list_a):
    n = len(list_a) # 10
    split =  n / 3 # 3.33333
    splited = n // 3 # 3
    mod = split % 1 # 0.33333
    if mod > 0:
        a = list_a[0:splited] # [28, 14, 13]
        b = list_a[len(a):splited*2] # [21, 19, 27]
        last = len(a + b) # 6
        c = list_a[last:] # [23, 30, 16, 3]
        #print(a)
        #print(b)
        #print(c)
        d = statistics.median(a) # 14
        e = statistics.median(b) # 21
        cal = c[-1] + c[-2] # 16+3
        new = [cal/2] # 9.5
        new_c = c[0:2] + new # [23, 30, 9.5]
        f = statistics.median(new_c) # 23
        #print(d)
        #print(e)
        #print(f)
        final = [d, e, f]
        result = statistics.median(final)
    return result


if __name__ == "__main__":
    main()