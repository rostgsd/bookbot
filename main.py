
def get_book_text(file):
    with open(file) as str:
        return str.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def main():
    text = get_book_text("/home/rostgsd/workspace/github.com/personal/bookbot/books/frankenstein.txt")
    word_count = count_words(text)
    print(f'{word_count} words found in the document')

main()