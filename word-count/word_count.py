PUNCTUATION_CHARACTERS = ['\n', '\t', '_', ':', '!', '&', ',', '@', '$', '%', '^', '.', '\' ', ' \'']

def word_count(phrase):

    words = clean_phrase(phrase)
    counter = {}

    for word in set(words):
        counter[word] = words.count(word)
    return counter


def clean_phrase(phrase):
    phrase = phrase.lower()
    for character in PUNCTUATION_CHARACTERS:
        if character in phrase:
            phrase = phrase.replace(character, ' ')
    words = phrase.split()
    return words
