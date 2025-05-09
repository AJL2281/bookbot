def get_num_words(text):
    count_words = 0

    split_words = text.split()

    for words in split_words:
        count_words += 1

    return count_words

def get_num_character(text):
    chars_dic = {}

    for char in text.lower():
        if char in chars_dic:
            chars_dic[char] += 1
        else:
            chars_dic[char] = 1
    
    return chars_dic

def get_dic_list(chars_dic):
    chars_list = []

    for char, count in chars_dic.items():
        chars_list.append({"char": char, "num": count})

    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
