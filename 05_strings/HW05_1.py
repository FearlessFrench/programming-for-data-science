#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW05_1
# 229223 Sec 001

def main():
    # input
    letter = input()
    remove = input()
    # output
    print(palindrome_without(letter, remove))


def palindrome(word):
    if len(word) < 1:
        return False
    if len(word) >= 1:
        # banana == ananab
        return word == word[::-1] # True


def palindrome_without(text, c):
    # Banana to banana
    text = text.lower()
    # remove "b"
    new_text = text.replace(c , "")
    # anana == anana
    result = palindrome(new_text)
    return result  # ==> True or False


def test_palindrome_without():
    assert test_palindrome_without("Banana", "b") == True
    assert test_palindrome_without("Swap of paws", "f") == True
    assert test_palindrome_without("T", "t") == False
    print("5..... \n4.... \n3... \n2.. \n1. \nHappy New Year 2023!")


if __name__ == "__main__":
    main()