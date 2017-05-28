def word_count(phrase):
    count = {}

    phrase = phrase.lower()
    phrase = phrase.replace('\n', ' ')
    phrase = phrase.replace('\t', ' ')
    phrase = phrase.replace(',', ' ')
    phrase = phrase.replace('_', ' ')
    for word in phrase:
        if not(word.isalnum()) and word != ' ':
            phrase = phrase.replace(word, '')
    split_word = phrase.split()

    for word in split_word:
        count[word] = split_word.count(word)

    return count

