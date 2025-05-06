#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# HW07_3
# 229223 Sec 001

def main():
    test_num_to_word()
    # input
    number = int(input())
    # output
    print(num_to_word(number))

def three_digits_to_word(n):  # n = (0 < n <= 999)
    unit_list = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    # >>> unit_list[17]
    # 'seventeen'
    unit_list_ten = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    h = ["hundred"]

    if n >= 100: # n = 999  # nine hundred ninety-nine
        x = divmod(n, 100) # ==> x = (9, 99)
        a = x[0]  #  9
        b = x[1]  # 99
        if b <= 19:
                word = unit_list[a] +" "+ h[0] +" "+ unit_list[b]
                return word 
        y = divmod(b, 10)  # ==> x = (9, 9)
        c = y[0]  # 9 (ten digit)
        d = y[1]  # 9 (first digit)
        word = unit_list[a] +" "+ h[0] +" "+ unit_list_ten[c] +"-"+ unit_list[d]
        return word
    elif n >= 20: # n = 86  # eighty-six
        x = divmod(n, 10) # ==> x = (8, 6)
        a = x[0]  # 8
        b = x[1]  # 6
        if b == 0:
            word = unit_list_ten[a]
            return word
        word = unit_list_ten[a] +"-"+ unit_list[b]
        return word
    else:
        return unit_list[n]


def num_to_word(num):  # num = (0 <= num)
    o = "zero"
    k = "thousand"
    m = "million"
    bl = "billion"
    t = "trillion"
    q = "quintillion"
    s = "sextillion"
    # Calling in three_digits_to_word(n)
    # 3862 ==> three thousand + (three_digits_to_word(862))
    if num == 0:
        return o
    elif num < 1000:
        return three_digits_to_word(num)
    elif num < 10000:
        x = divmod(num, 1000)
        a = x[0] # 3
        b = x[1] # 862
        word = three_digits_to_word(a) +" "+ three_digits_to_word(b)
        return word
    # 64132 ==> sixty four + (three_digits_to_word(132))
    elif num < 100000:
        x = divmod(num, 1000)
        a = x[0] # 64
        b = x[1] # 132  
        word = three_digits_to_word(a) +" "+ k +" "+ three_digits_to_word(b)
        return word
    # 124865 ==> (three_digits_to_word(124)) + thousand + (three_digits_to_word(865))
    elif num < 1000000:
        x = divmod(num, 1000)
        a = x[0] # 124
        b = x[1] # 865    
        word = three_digits_to_word(a) +" "+ k +" "+ three_digits_to_word(b)      
        return word
    # 2128735 ==> two + million + (three_digits_to_word(128)) + thousand + (three_digits_to_word(735))
    elif num < 10000000:
        x = divmod(num, 1000000)
        a = x[0] # 2
        b = x[1] # 128735
        y = divmod(b, 1000)
        c = y[0] # 128
        d = y[1] # 735
        word = (three_digits_to_word(a)) +" "+ m +" "+ (three_digits_to_word(c)) +" "+ k +" "+ (three_digits_to_word(d))
        return word
    # 42641323862
    else:
        x = divmod(num, 1000000000)
        a = x[0] # 42
        b = x[1] # 641323862
        y = divmod(b, 1000000)
        c = y[0] # 641
        d = y[1] # 323862
        z = divmod(d, 1000)
        e = z[0] # 323
        f = z[1] # 862
        word = three_digits_to_word(a) +" "+ bl +" "+ three_digits_to_word(c) +" "+ m +" "+ (three_digits_to_word(e)) +" "+ k +" "+ (three_digits_to_word(f))
        return word        
    

def test_num_to_word():
    assert num_to_word(14) == "fourteen"
    assert num_to_word(248) == "two hundred forty-eight"    
    assert num_to_word(111) == "one hundred eleven"
    assert num_to_word(0) == "zero"   
    assert num_to_word(42641323862) == "forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two"    
    print("Superb!!!")

if __name__ == '__main__':
    main()