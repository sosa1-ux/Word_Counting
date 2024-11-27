#count_spaces

def count_words(word_count):
    if word_count > 1:
        raise ValueError("The phrase exceeds two words, limit your entry to single words or two word phrases. Exiting Program.")
    elif word_count == 0:
        return("Standby")
    else:
        return("searching...")