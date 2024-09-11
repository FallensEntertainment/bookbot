def main():
    book_path = "books/frankenstein.txt"
    file_contents = book_text(book_path)
    num_words =  wordCount(file_contents)
    chars_dict = lettersCount(file_contents)
    report_list = []
    for char, count in chars_dict.items():
        temp_dict = {'char': char, 'num': count}
        report_list.append(temp_dict)
    report_list.sort(reverse=True, key=sort_on)    
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {num_words} words in this book.")
    for item in report_list:
        print(f"The {item['char']} character was found {item['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def book_text(path):
    with open(path) as f:
        return f.read()
    
def wordCount(file_contents):
    words = file_contents.split()
    return len(words)

def lettersCount(characters):
    lower_case = characters.lower()
    letters = {}
    for letter in lower_case:
        if letter.isalpha():
            letters[letter] = letters.get(letter, 0) + 1
    return letters


main()
