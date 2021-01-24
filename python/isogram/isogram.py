def is_isogram(string):
    word_cleared = string.replace(" ", "").replace("-", "").lower()
    return len(word_cleared) == len(set(word_cleared))