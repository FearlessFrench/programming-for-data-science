#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab10_2
# 229223 Sec 001

def main():
    test_comma_separated()
    x = int(input())
    digit = int(input())
    print(comma_separated(x, digit))


def comma_separated(n, digit=3):
    s = str(n)  # "3400"
    if len(s) == digit:
        return s
    else:
        comma = s[-(digit)-1] + "," + s[-(digit):] # "3,400"
        result = comma
        return result


def test_comma_separated():
    assert comma_separated(3400, digit=3) == "3,400"
    assert comma_separated(3400, digit=4) == "3400"
    assert comma_separated(781588, digit=5) == "7,81588"
    assert comma_separated(1234, digit=3) == "1,234"
    print("Saul Goodman")

if __name__ == "__main__":
    main()