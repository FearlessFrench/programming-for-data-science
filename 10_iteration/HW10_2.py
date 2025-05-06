#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW10_2
# 229223 Sec 001

def main():
    x = 20
    print('----')
    print(eratosthenes(x, True))


def eratosthenes(n, show_step=False):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            print(p, end=" ")         


if __name__ == "__main__":
    main()