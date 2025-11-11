from stats import get_num_words
from stats import count_characters
from stats import sort_dict
from stats import sort_on

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    total_characters = count_characters(text)
    #print(num_words)
    #print(total_characters)
    

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    

main()
