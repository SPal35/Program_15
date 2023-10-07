def sort_words(input_sequence):
    words = input_sequence.split(',')
    sorted_words = sorted([word.strip() for word in words])
    sorted_sequence = ', '.join(sorted_words)
    return sorted_sequence
input_sequence = input("Enter a comma-separated sequence of words: ")
sorted_sequence = sort_words(input_sequence)
print("Words in alphabetical order:", sorted_sequence)
