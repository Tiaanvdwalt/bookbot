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


def sort_on(items):
    return items["num"]

def sort_dict(total_characters):
    sorted_text = total_characters.sort(key=sort_on)
    return sorted_text