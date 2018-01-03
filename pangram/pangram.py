ALPHABET_LEN = 26


def is_pangram(sentence):
    sentence_latters = list(filter(str.isalpha, sentence.lower()))
    return ALPHABET_LEN == len(set(sentence_latters))
