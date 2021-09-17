import string

def clean_word(word):
    translator = str.maketrans('','', string.punctuation)
    word = word.translate(translator)
    word = word.lower()
    word = word.strip()
    return word
