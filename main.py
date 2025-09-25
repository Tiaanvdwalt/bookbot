from stats import get_num_words
from stats import count_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    total_characters = count_characters(text)
    print(num_words)
    print(total_characters)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    

main()
