#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW05_3
# 229223 Sec 001

def main():

    # input
    toyota = str(input())
    opel = str(input())
    nissan = str(input())
    # output
    print(substitute_once(toyota, opel, nissan))


def substitute_once(text, old, new):
    # "battlefield", "b", "c"
    # "battlefield".replace(old, new, (count=1))
    # (count=1) คือ แทนที่ 1 ครั้ง
    result = text.replace(old, new, 1)
    return result

def test_substitute_once():
    assert test_substitute_once("battle", "b", "c") == "cattle"
    assert test_substitute_once("Bidding", "i", "u") == "Budding"
    assert test_substitute_once("doesn't", "n't", " not") == "does not"
    print("Battlefield to Cattlefield")



if __name__ == "__main__":
    main()