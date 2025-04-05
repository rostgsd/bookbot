
def get_book_text(file):
    with open(file) as str:
        return str.read()    
        
def main():
    from stats import count_words

    text = get_book_text("/home/rostgsd/workspace/github.com/personal/bookbot/books/frankenstein.txt")
    word_count = count_words(text)
    print(f'{word_count} words found in the document')

main()