def missing_chars(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = word.lower()
    missing = ''

    for char in alphabet:
        if char not in word:
            missing += char

    return missing

word = 'The quick brown fox'
print(missing_chars(word))