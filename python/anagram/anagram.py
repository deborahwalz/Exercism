def find_anagrams(word, candidates):
    return [
        cand for cand in candidates
        if sorted(cand.lower()) == sorted(word.lower()) and cand.lower() != word.lower() 
    ]