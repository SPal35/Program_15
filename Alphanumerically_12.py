def remove_duplicates_and_sort(input_words):

    words = input_words.split()


    unique_words = list(set(words))

    sorted_unique_words = sorted(unique_words)

    return sorted_unique_words

input_words = input("Enter whitespace-separated words: ")

sorted_unique_words = remove_duplicates_and_sort(input_words)

print("Sorted unique words:", ' '.join(sorted_unique_words))
