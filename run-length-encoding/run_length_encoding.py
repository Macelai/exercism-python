def decode(word):
    decoded = ""
    number = ""
    for i in range(len(word)):
        if word[i].isdigit():
            number += word[i]
        else:
            if number == "":
                number = "1"
            decoded += int(number) * word[i]
            number = ""
    return decoded

def encode(word):
    count = 1
    word = word + "\n"
    str_encoded = ""
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            count += 1
        else:
            if count == 1:
                str_encoded += word[i]
            else:
                str_encoded += str(count) + word[i]
            count = 1
    return(str_encoded)
