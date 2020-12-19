import string

def is_pangram(sentence):
    sentence = sentence.lower()
    chrs = string.ascii_lowercase
    idx = [chr in sentence for chr in chrs]
    return sum(idx) == 26

if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog."))
    print(is_pangram("Five quacking Zephyrs jolt my wax bed."))