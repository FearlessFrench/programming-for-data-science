#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab13_2
# 229223 Sec 001

def main():
    board = [[2, 7, 6],
             [9, 5, 1],
             [4, 3, 8]]
    print(is_magic_square(board))


def is_magic_square(board):
    # horizontal
    count1 = 0
    for i in range(len(board[0])): # loop in board 3 => 0 1 2
        #for j in range(len(board)): # main loop 3 => 0 1 2
        a = board[0][i]
        count1 += a
    #print(count1)
    # vertical
    count2 = 0
    for j in range(len(board[0])): # 0 1 2
        b = board[j][0]
        count2 += b
    #print(count2)
    # diagonal
    count3 = 0
    for k in range(len(board[0])): # 0 1 2
        c = board[k][k]
        count3 += c
    #print(count3)
    # check if repeat
    for l in range(len(board[0])): # 0 1 2
        for m in range(len(board[0])):
            d = board[l][m]

    if count1 == count2 and count1 == count3:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

