#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW13_1
# 229223 Sec 001

def main():
    list_x = [[2, 3, 4],
              [1, 2, 3]]
    print(square_matrix(list_x))


def square_matrix(list_x):
    # column = 3
    # row = 2
    # if column = 3 then row = 3 too
    for i in range(len(list_x[0])): # 0 1 2
        # create a list [0, 0, 0]
        a = list_x[0][i]
    list_x.append([0,0,0])
    return list_x

if __name__ == "__main__":
    main()