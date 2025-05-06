#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW14_1
# 229223 Sec 001

import math

def main():
    matrix = [[1, 2],
[1, 2, 3],
[1, 2],
[1, 2],
[1]]

    print(reshape(matrix))


def reshape(matrix):
    # row <= column
    a = 0
    for i in range(len(matrix)):
        x = len(matrix[i])
        a += x
    print(a) # 9
    if len(matrix) == a//3:
        return matrix
    else:
        f = []
        s = []
        t = []
        f += [matrix[0][0]] + [matrix[0][1]] + [matrix[1][0]] + [matrix[1][1]]
        s += [matrix[1][2]] + [matrix[2][0]] + [matrix[2][1]] + [matrix[3][0]]
        t += [matrix[3][1]] + [matrix[4][0]]
        #print(f)  
        #print(s)            
        #print(t)
        matrix = [f] + [s] + [t]
        #print(matrix)
        if len(matrix[0]) != len(matrix[-1]):
            matrix[-1].append(0)
            matrix[-1].append(0)
            return matrix
        


        
if __name__ == "__main__":
    main()