def to_rna(dna_strand):
    """
    Given a DNA strand, return its RNA complement (per RNA transcription).
    """
    dna = [i for i in dna_strand]
    rna = ""

    # Define the dictionary mapping
    switcher = {
        "A": "U",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    for i in dna:
        rna += switcher.get(i) # search for the key i, return the corresponding value

    return rna