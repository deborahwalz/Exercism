def is_isogram(string):
    word_cleared = [s.lower() for s in string if s.isalpha()]
    return len(word_cleared) == len(set(word_cleared))