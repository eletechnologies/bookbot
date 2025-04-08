def number_of_words(book_text):
    word_count = len(book_text.split())
    # print(f"{word_count} words found in the document")
    return word_count

def letter_count(book_text):
    letter_dict = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char not in  letter_dict:
            letter_dict[lower_char] = 1
        else:
            letter_dict[lower_char] += 1
    return letter_dict

def sorted_letter_counts(raw_letter_dict):
    completed_list = []
    sorted_letters = dict(sorted(raw_letter_dict.items(), reverse=True, key=lambda item: item[1]))
    for k, v in sorted_letters.items():
        completed_list.append({"letter":k, "count":v})
    return completed_list

    

