#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# Lab08_2
# 229223 Sec 001

def main():
    x = 1234 #int(input("x = "))
    print(reverse_digits(x)) # 4321

def reverse_digits(x):
    if x == 0:
        return 0
    else:  
        return reverse_digits(x//10) + (x%10)

if __name__ == "__main__":
    main()