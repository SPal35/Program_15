def calculate_letter_case_count(sentence):
    upper_count = 0
    lower_count = 0

    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

sentence = input("Enter a sentence: ")

upper_count, lower_count = calculate_letter_case_count(sentence)

print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
