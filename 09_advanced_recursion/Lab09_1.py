#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab09_1
# 229223 Sec 001

def main():
    string1 = "cat"
    string2 = "Act"
    print(is_anagram(string1, string2))


def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2:
        return True
    else:
        return False


def test_is_anagram():
    assert is_anagram("Tom Marvolo Riddle", "I am Lord Voldermort") == True
    assert is_anagram("cat", "tab") == False
    print("Simulation Completed")


if __name__ == "__main__":
    main()