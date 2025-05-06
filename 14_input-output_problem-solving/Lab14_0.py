#!/usr/bin/env python3
# Panutad Sirikul (French)
# 641510230, 650510714
# Lab14_0
# 229223 Sec 001
import math

def main():
    list_a = [(2, 7, 1.5), (3.2, 2.5, 4.06), (-5.5, -4.5, 2.5), (2, -5.2, 3),(7.2, -2.8, 1.2)]
    print(count_segment(list_a))

def  count_segment(list_a):

    # counting Quadrant from (px, py)
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0

    for i in list_a:  # len(a) = 5
        x, y, r = i
        d = math.sqrt(x**2 + y **2)
        if x == 0 and y == 0:
            num1 +=1
            num2 +=1
            num3 +=1
            num4 +=1
            continue

        elif x == 0:
            if y > 0:
                num1 +=1
                num2 +=1
                if y - r < 0:
                    num3 +=1
                    num4 +=1
            else:
                num3 +=1
                num4 +=1
                if y + r > 0:
                    num1 +=1
                    num2 +=1
            continue

        elif y == 0:
            if x > 0:
                num1 += 1
                num4 += 1
                if x - r < 0:
                    num2 +=1
                    num3 +=1
            else:
                num2 +=1
                num3 +=1
                if x + r > 0:
                    num1 +=1
                    num4 +=1
            continue
        
        else:
            # q1
            if x > 0 and y > 0:  # ++
                num1 += 1
                if x - r < 0:
                    num2+=1
                if y - r < 0:
                    num4+=1
                if d - r < 0:
                    num3+=1

            #q2
            elif x < 0 and y > 0: #-+
                num2 += 1
                if x + r > 0:
                    num1 +=1
                if y - r < 0:
                    num3 +=1
                if d - r < 0:
                    num4 +=1

            #q3
            elif x < 0 and y < 0:  # --
                num3 += 1
                if x + r > 0:
                    num4+=1
                if y + r > 0:
                    num2+=1
                if d -r < 0:
                    num1+=1                
            
            #q4
            else:
                num4 += 1
                if x - r < 0:
                    num3+=1
                if y + r > 0:
                    num1+=1
                if d - r < 0:
                    num2+=1
    return num1, num2, num3, num4



if __name__ == "__main__":
    main()