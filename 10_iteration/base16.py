def decimal_to_hexadecimal(dec):
    first_v = str(dec)[0]
    decimal = int(dec)
    if first_v == '-': 
        hex_dec = hex(decimal)[3:]
    else:
        hex_dec = hex(decimal)[2:]
    return hex_dec

result = decimal_to_hexadecimal(0.9375)

print('result : ', result)