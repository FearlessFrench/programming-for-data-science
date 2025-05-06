#!/usr/bin/env python3
# Panutad Sirikul
# 650510714
# HW06_1
# 229223 Sec 00B


def main():

    print(decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 .
'''))


def decode_helper(code_table, str_index):  # รับรหัส 1 ตัว แล้วคืน 1 อักขระที่ถูกต้อง
    # take '0' return 'a'
    code_table = ["a","c",'e','i','k','l','m','r',"-",'_','\n']    
    str_index  = ['0','1','2','3','4','5','6','7','8','86','.']
    if str_index == '0':
        code_table = "a"
        return code_table
    if str_index == '1':
        code_table = "c"
        return code_table
    if str_index == '2':
        code_table = "e"
        return code_table
    if str_index == '3':
        code_table = "i"
        return code_table
    if str_index == '4':
        code_table = "k"
        return code_table
    if str_index == '5':
        code_table = "l"
        return code_table
    if str_index == '6':
        code_table = "m"
        return code_table
    if str_index == '7':
        code_table = "r"
        return code_table
    if str_index == '8':
        code_table = "-"
        return code_table
    if str_index == '86':
        code_table = "_"
        return code_table
    if str_index == '.':
        code_table = "\n"
        return code_table



def decode(code_table, text):
    # แยกรหัสทั้งหมด ให้กลายเป็น list เช่น ['3', '.', '5', '3', '4', '2', '.', ...]
    l_text = text.split()
    # l_text = ['3', '.', '5', '3', '4', '2', '.', '3', '1', '2', '8', '1', '7', '2', '0', '86', '.']

    # เรียกใช้ฟังก์ชัน decode_helper() ที่มีหน้าที่รับรหัสหนึ่งตัว แล้วคืน 1 อักขระที่ถูกต้อง
    result_list = list(map(lambda x: decode_helper(code_table, x), l_text))

    # รวม list ของอักขระ ให้เป็น string
    result = ''.join(result_list)
    return result


if __name__ == '__main__':
    main()
