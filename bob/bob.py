def hey(phrase):
    phrase = phrase.replace("\t", "")
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace("\n", "")
    phrase = phrase.replace("\r", "")

    if len(phrase) == 0:
        return("Fine. Be that way!")
    elif phrase.isupper():
        return("Whoa, chill out!")
    elif phrase[len(phrase)-1] == "?":
        retur("Sure.")
    else:
        return("Whatever.")
