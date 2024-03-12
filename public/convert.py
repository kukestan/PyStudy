def decimal_to_base(decimal_num, base):
    if base < 2 or base > 36 or int(base) != base:  
        raise ValueError("Base must be an integer greater than or equal to 2")

    if decimal_num == 0:  
        return '0'
    elif base == 2:
        return bin(decimal_num)
    elif base == 8:
        return oct(decimal_num)
    elif base == 16:
        return hex(decimal_num)
    else:
        remainder = decimal_num % base
        if remainder > 10:
            remainder_str = str(chr(remainder - 10 + ord('A')))
        else:
            remainder_str = str(remainder) 
        if decimal_num < base:
            return remainder_str
        else:
            return decimal_to_base(decimal_num // base, base) + remainder_str

def convert_to_decimal(number_str, base):  
    try:  
        # 使用int函数将任意进制的数转换为10进制数  
        decimal_number = int(number_str, base)  
        return decimal_number  
    except ValueError as e:  
        print(f"转换出错: {e}")  
        return None 

print(decimal_to_base(71, 36))
print(convert_to_decimal('1Z', 36))