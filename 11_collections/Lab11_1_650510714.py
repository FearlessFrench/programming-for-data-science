#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab11_1
# 229223 Sec 001


def main():
    input = "He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."
    print(word_count(input))

def word_count(text):
    text_lower = text.lower() # lowercase text
    list_text = text_lower.split() # change string to list
    list_dict = {} # create an empty set
    for i in list_text:
        if i in list_dict:
            list_dict[i] += 1
        else:
            list_dict[i] = 1
    count = list_dict
    return count


if __name__ == '__main__':
    main()
