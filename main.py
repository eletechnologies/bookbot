from stats import number_of_words
from stats import letter_count
from stats import sorted_letter_counts
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def main():
    # number_of_words(get_book_text("books/frankenstein.txt"))
    character_count = letter_count(get_book_text(sys.argv[1]))
    # total_character_count = 0
    # for v in character_count.values():
    #     total_character_count += v

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    final_list_sorted = sorted_letter_counts(character_count)

    for character in final_list_sorted:
        if character["letter"].isalpha():
            print(f"{character["letter"]}: {character["count"]}")
    
    print("============= END ===============")

main()
