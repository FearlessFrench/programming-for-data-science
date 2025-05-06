#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW08_2
# 229223 Sec 001

def main():
    ms = "123"
    pt = "** *** ** ** *"
    print(patterned_message(ms, pt))


def patterned_message(message, pattern):
    return patterned_message(message, pattern.replace("*", message))



if __name__ == "__main__":
    main()