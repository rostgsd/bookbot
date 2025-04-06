
def get_book_text(file):
    with open(file) as str:
        return str.read()    

import sys 
from stats import count_words, count_chars, order_letters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

text = get_book_text(book_path)
word_count = count_words(text)
char_counts = order_letters(count_chars(text))

def report():
    print( '============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char in char_counts:
        print(f'{char['letter']}: {char['freq']}')
    print('============= END ===============')

def main():
    report()

main()
        
    
