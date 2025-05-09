import sys
from stats import (get_num_words, get_num_character, get_dic_list)

def get_book_text(p):
    with open(p) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    file_path = sys.argv[1]

text = get_book_text(file_path)
counted_words = get_num_words(text)
char_counts = get_num_character(text)
sorted_chars = get_dic_list(char_counts)

print('============ BOOKBOT ============')
print(f'Analyzing book found at {file_path}...')
print('----------- Word Count ----------')
print(f'Found {counted_words} total words')
print('--------- Character Count -------')
for char_dict in sorted_chars:
    if char_dict["char"].isalpha():
        print(f'{char_dict['char']}: {char_dict['num']}')
print('============= END ===============')