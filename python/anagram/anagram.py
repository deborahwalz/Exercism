def find_anagrams(word, candidates):
    word_counts = {s: word.lower().count(s) for s in set(word.lower())}
    candidates = [cand for cand in candidates if cand.lower() != word.lower()]
    anagrams = [
        cand for cand in candidates
        if {s: cand.lower().count(s) for s in set(cand.lower())} == word_counts
    ]
    return anagrams