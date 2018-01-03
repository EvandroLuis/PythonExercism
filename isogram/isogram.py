def is_isogram(string):
    s = list(filter(str.isalnum, string.lower()))
    return len(s) == len(set(s))
