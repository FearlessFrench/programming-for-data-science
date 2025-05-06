#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab07_1
# 229223 Sec 001 

def main():
    # input
    x = str(input())
    # output
    print(corner_frame(x))

def corner_frame(n): # (n ≥ 2)
    # Base Case
    if n == '1':
        return
    # Divide & Conquer
    x = int(n)
    y = list(map(str, range(1,x+1))) # ['1', '2', '3', '4']
    p = " " 
    m = '\n'
    z = p.join(y)


    d = (str(x-5) + p)*(x-5) + z[(x*2-10):]
    e = (str(x-4) + p)*(x-4) + z[(x*2-8):]
    f = (str(x-3) + p)*(x-3) + z[(x*2-6):]
    g = (str(x-2) + p)*(x-2) + z[(x*2-4):]
    h = (str(x-1) + p)*(x-1) + z[(x*2-2):]
    frame = (str(x) + p)*x + z[(x*2):]
    # Combine
    if n == '2':
        return z+m+frame
    elif n == '3':
        return z+m+h+m+frame
    elif n == '4':
        return z+m+g+m+h+m+frame
    elif n == '5':
        return z+m+f+m+g+m+h+m+frame
    elif n == '6':
        return z+m+e+m+f+m+g+m+h+m+frame
    elif n == '7':
        return z+m+d+m+e+m+f+m+g+m+h+m+frame
    else:
        return frame




if __name__ == '__main__':
    main()







































































    