def is_divisible_by_5(binary_numbers):
    divisible_by_5 = []
    
    for binary_num in binary_numbers:
        decimal_num = int(binary_num, 2)  
        if decimal_num % 5 == 0:
            divisible_by_5.append(binary_num)
    
    return divisible_by_5

binary_numbers_input = input("Enter comma-separated 4-digit binary numbers: ")

binary_numbers = binary_numbers_input.split(',')

divisible_by_5_numbers = is_divisible_by_5(binary_numbers)
print("Numbers divisible by 5:", ', '.join(divisible_by_5_numbers))
