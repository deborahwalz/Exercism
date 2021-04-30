def is_isogram(string):
    word_cleared = [s for s in string.lower() if s.isalpha()]
    return len(word_cleared) == len(set(word_cleared))