#!/usr/bin/env python3
# Panutad Sirikul (French)
# 650510714
# Lab05_1
# 229223 Sec 001

# ให้เขียนฟังก์ชัน german_num_format(num_str) เพื่อคืนค่า String
# แทนตัวเลขในรูปแบบที่ใช้ในประเทศเยอรมนีเมื่อ num_str เป็น string แทนตัวเลขจ านวนจริงในรูปแบบปกติที่ใช้
# ในประเทศไทยที่มีการใช้comma หรือ จุลภาค (,) เป็น thousand separator (คั่นจ านวนเลขนับจากหลักหน่วยไปที
# ละ 3 หลัก) และ period หรือ จุด/มหัพภาค (.) แทนจุดทศนิยม

def main():
    test_german_num_format()
    # input
    x = str(input())
    # output
    print(german_num_format(x))


def german_num_format(num_str): # 1,020.50 => 1.020,50
    # 1,020.50 => 1c020d50 => 1.020,50
    f_num_str = num_str.replace("." , "d")     # 1,020d50
    s_num_str = f_num_str.replace("," , "c")   # 1c020d50
    t_num_str = s_num_str.replace("c" , ".")   # 1.020d50
    new_num_str = t_num_str.replace("d" , ",") # 1.020,50

    return new_num_str
    
    

def test_german_num_format():
    assert german_num_format("1,234") == "1.234"
    assert german_num_format("1,020.50") == "1.020,50"
    assert german_num_format("4,783.64") == "4.783,64"
    print("all ok!")


if __name__ == '__main__':
    main()