
def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    letters_dict = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0
    }
    characters = list(text)
    for character in characters:
        if character in letters_dict:
            letters_dict[character] += 1
    return letters_dict

def order_letters(letters): # dict
    # create a list of dicts 'cache' for compatibility
    cache = []
    for letter in letters:
        cache.append({ 'letter':letter, 'freq':letters[letter]})
    # carrier function
    def sort_on(dict):
        return dict["freq"]
    # sort cache and return
    cache.sort(reverse=True, key=sort_on)
    return cache

