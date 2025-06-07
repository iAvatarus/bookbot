def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(content):
    return len(content.split())

def get_num_characters(content):
    content = content.lower()
    charset = set(content)
    char_dict = dict()
    for char in charset:
        char_dict[char] = content.count(char)
    return char_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_list(char_dict):
    new_list = []
    for char in char_dict:
        new_list.append({"char": char, "num": char_dict[char]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

