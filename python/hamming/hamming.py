def distance(strand_a, strand_b):
    """Calculate the Hamming Distance between two DNA strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError("The Hamming Distance is only defined for sequences of equal length!")
    return sum([a != b for a, b in zip(strand_a, strand_b)])