def decimal_to_hexdecimal(decimal_num):
    hex_characters="0123456789ABCDEF"
    if decimal_num==0:
        return "0"
    hexadecimal=""
    while decimal_num>0:
        remainder = decimal_num % 16
        hexadecimal = hex_characters[remainder]+ hexadecimal
        decimal_num //=16
    return hexadecimal

decimal_number=int(input("enter a number: "))
hexadecimal_value= decimal_to_hexdecimal(decimal_number)
print(hexadecimal_value)
