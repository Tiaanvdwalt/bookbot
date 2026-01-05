def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    book_text = text.lower()
    for char in book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def list_of_dicts(dict):
    list_of_dicts = [{"char": k, "num": v} for k, v in dict.items() if k.isalpha()]
    return list_of_dicts

def sort_on(items):
    return items["num"]