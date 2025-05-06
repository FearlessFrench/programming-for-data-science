#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW13_EX
# 229223 Sec 001

def main():
    sand = [9, 12, 6]
    print(sand_towers(sand))

def sand_towers(list_a):
    a = '''
        |>>~
        |
      /^^^\\
     /     \\   
    /^^^^^^^\\'''

    b = '''
      /^^^\\
     /     \\   
    /^^^^^^^\\'''

    c = '''
   /         \\'''    
    
    base = ":::::::::"
    for i in range(list_a[0]-3):
        print(i)
        d = b+c*i+base
    for j in range(list_a[1]-3):
        print(i)
        e = a+c*j+base
    for k in range(list_a[2]-3):
        print(i)
        f = b+c*k+base
    return d+e+f


if __name__ == "__main__":
    main()