#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab12_2
# 229223 Sec 001

def main():
    t = (10, -1, 1, -8, 3, 1)
    target_value = (7)
    print(matching_sum(t, target_value))

def matching_sum(t, target_value) :
    for i in range(len(t)):
        if target_value in t: 
            return target_value



if __name__ == "__main__":
    main()