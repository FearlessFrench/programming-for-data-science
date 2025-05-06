#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab13_1
# 229223 Sec 001

def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[7, 8, 5, 9, 3], [9, 10, -3, 7, 13], [11, 12, 6, 2, 9]] #[[7, 8], [9, 10], [11,12]]
    print(matrix_mult(m1, m2))
    
def matrix_mult(m1, m2):
    n = 0
    m = 0
    o = 0 
    p = 0
    for i in range(len(m1)): # loop นอก 0 1
        for j in range(len(m2)): # loop ใน 0 1 2
            x = m1[i][j] * m2[j][i]
            y = m1[i][j] * m2[j][i+1]
            n += x
            m += y
            #print([x, y])
        for k in range(len(m2)): # loop ใน 0 1 2
            a = m1[i+1][k] * m2[k][i]
            b = m1[i+1][k] * m2[k][i+1]
            o += a
            p += b
            #print([a, b])
        return [[n, m], [o, p]]

if __name__ == "__main__":
    main()