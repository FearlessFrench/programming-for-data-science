#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# Lab06_2
# 229223 Sec 001

def main():
    # input
    x = str(input("Enter a list: ")) # [10, 'hello', 23.5, 4]
    # output
    print(classify(x))

    #• list_a (มีสมาชิกเป็นชนิด int) 
    #• list_b (มีสมาชิกเป็นชนิด float)
    #• list_c (มีสมาชิกเป็นชนิด str) 

def classify(list_x):
    x = list_x
    if x[0] is int:
        list_a = x[0]
        list_a = list(map(int, list_a))
        return list_a
    if x[1] is str:
        list_c = x[1]
        return list_c
    if x[2] is int:
        list_b = x[2]
        list_b = list(map(float, list_b))
        return list_b

    result = list_a + "\n" + list_b + "\n" + list_c
    return result


def test_classify():
    assert classify(1) == 1
    print("HALO")


if __name__ == '__main__':
    main()