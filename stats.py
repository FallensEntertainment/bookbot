def get_num_words(text):
    words = text.split()
    word_count = 0
    
    for word in words:
        word_count += 1
    
    return word_count

def get_num_letters(text):
    letter_count = {}

    for ch in text.lower():
        letter_count[ch] = letter_count.get(ch, 0) + 1
    
    return letter_count

def get_report(letters):
    report_list = []
    for ch, n in letters.items():
        report_list.append({"char": ch, "num": n})
    return report_list

def sort_on(item):
    return item["num"]

def sort_report(report_list):
    report_list.sort(key=sort_on, reverse=True)