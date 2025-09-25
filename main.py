from stats import *
import sys

print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = get_num_words(text)

    report_list = get_report(get_num_letters(text))
    sort_report(report_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in report_list:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")

    print("============= END ===============")       

if __name__ == "__main__":
    main()