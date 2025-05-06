#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW13_2
# 229223 Sec 001

def main():
    list_x = [3, 7, 4, 9, 5, 2, 6]
    simplified_m_sort(list_x, True)
    print('--------')
    print(list_x)
    

def simplified_m_sort(list_x, show_step=False):
    a = list(map(lambda x: [x], list_x))
    b = list(map(lambda x: x, a))
    if show_step == True:
        print(a)
        print(b)


if __name__ == "__main__":
    main()