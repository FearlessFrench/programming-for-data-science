#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW09_1
# 229223 Sec 001

def main():
    test_life_path()
    # input
    x = int(input("input number = "))
    # output
    print(life_path(x))


def life_path(n):
    if n < 10 and n > 0:
        return n
    else:
        # 13092004 => 1+3+0+9+2+0+0+4 = 19
        a = n%10 + life_path(n//10) # 19
        return a//10 + a%10 # 1+9


def test_life_path():
    assert life_path(13092004) == 1
    assert life_path(7) == 7
    assert life_path(35) == 8
    print("Simulation Completed")


if __name__ == "__main__":
    main()
