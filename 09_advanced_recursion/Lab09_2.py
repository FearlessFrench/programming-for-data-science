#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab09_2
# 229223 Sec 001

def main():
    x = 2   # x > 1
    y = 3    # y >= x and y > 1
    print(sum_prime_in_range(x, y))

def is_prime(x, y):
    if x < 2 and y < 2:
        return False
    elif y % x == 0:
        return False
    return True

def list_primes_in_range(x, y):
    # Use a list comprehension to find all prime numbers in the range
    prime_list = list(range(x, y+1))
    return [prime_list if is_prime(x, y)]

# 3 to 20 has prime number consisting of [3,5,7,11,13,17,19]
# Sum of [3,5,7,11,13,17,19] is 75
def sum_prime_in_range(x, y):
    if x <= 1 and y <= 1: 
        return 0
    else:
        return 0


def test_sum_prime_in_range():
    assert sum_prime_in_range(3, 20) == 75
    assert sum_prime_in_range(3, 3) == 3
    print("Simulation Completed")


if __name__ == "__main__":
    main()
