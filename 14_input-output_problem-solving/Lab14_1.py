#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab14_1
# 229223 Sec 001

def main():
    list_a = [[2, 3, 4, 5], 
              [8, 7, 6, 5], 
              [0, 1, 2, 3]]
    list_b = [[2, 3, 4, 5], 
              [8, 7, 6, 5], 
              [0, 1, 2, 3]]
    row = 1
    col = 2
    print(remove_row_col(list_a, row, col))


def remove_row_col(list_a, row, col):
    for i in range(len(list_a)): # 3
        # remove column
        del list_a[i][col]
    del list_a[row]
    return list_a



if __name__ == "__main__":
    main()