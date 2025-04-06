
def get_book_text(file):
    with open(file) as str:
        return str.read()    

from stats import count_words, count_chars, order_letters

text = get_book_text("/home/rostgsd/workspace/github.com/personal/bookbot/books/frankenstein.txt")
word_count = count_words(text)
char_counts = order_letters(count_chars(text))

def report():
    print( '============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char in char_counts:
        print(f'{char['letter']}: {char['freq']}')
    print('============= END ===============')

def main():
    report()

main()
        
    
