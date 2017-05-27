import string

def is_pangram(word):
    word = word.lower()
    alphabet = string.ascii_lowercase
    for char in word:
        for alpha in alphabet:
            if word.count(alpha) <= 0:
                return False
        return True
