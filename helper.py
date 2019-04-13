def is_isbn_or_key(word):
    # ISBN ISBN13 \d{13} ISBN10 [0-9]{10}含有"-"
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and short_word == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
