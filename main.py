from stats import get_num_words
from stats import count_characters
from stats import list_of_dicts
from stats import sort_on

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    total_characters = count_characters(text)
    dict_list = list_of_dicts(total_characters)
    dict_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============\n"
          f"Analyzing book found at {book_path}...\n"
          "----------- Word Count ---------- \n"
          f"Found {num_words} total words \n"
          "--------- Character Count -------")
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    

main()
