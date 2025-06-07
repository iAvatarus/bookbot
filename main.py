from stats import get_book_text, get_num_words, get_num_characters, get_sorted_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    content = get_book_text(path)
    print(f"Analyzing book found at {path}...")
    num_words = get_num_words(content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    num_chars = get_num_characters(content)
    sorted_list = get_sorted_list(num_chars)
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    return


main()