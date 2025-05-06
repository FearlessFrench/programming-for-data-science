#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab07_2
# 229223 Sec 001

import re

def main():
    test_uniform()
    # input
    letter = str(input()) # HaPpY
    # output
    print(uniform(letter)) # HAPPY

def uniform(line):
    # Base Case?

    # Divide
    ucase = re.findall(r"[A-Z]", line)
    lcase = re.findall(r"[a-z]", line)
    # Conquer
    N = len(ucase) # counting A-Z
    n = len(lcase) # counting a-z
    
    # Combine
    if N > n:
        return line.upper()
    elif n > N:
        return line.lower()
    elif N == n:
        x = line[0]
        if x == x.upper():
            return line.upper()
        else:
            return line.lower()


def test_uniform():
    assert uniform('HaPpY') == 'HAPPY'
    assert uniform('cOdINg') == 'coding'
    assert uniform('coMP scI!!!') == 'comp sci!!!'
    print("Alright!")


if __name__ == '__main__':
    main()