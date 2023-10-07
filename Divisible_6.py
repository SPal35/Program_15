divisible_by_7_not_multiple_of_5 = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]

print(','.join(divisible_by_7_not_multiple_of_5))
