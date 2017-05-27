def is_isogram(word):
    word = word.lower()
    word = word.replace(" ", "")
    word = word.replace("-", "")
    for char in word:
        if word.count(char) > 1:
            return False
    return True
