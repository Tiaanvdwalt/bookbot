def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words():
    counter = 0
    book_text = get_book_text("books/frankenstein.txt")
    words = book_text.split()
    for word in words:
        counter += 1
    total_word_count = f"{counter} words found in the document"
    print(total_word_count)
    return total_word_count

def count_characters():
    counter = 0
    book_text = get_book_text("books/frankenstein.txt").lower()
    print(book_text)
    




count_characters()