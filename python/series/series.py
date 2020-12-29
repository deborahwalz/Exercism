def slices(series, length):
    """
    Given a string of digits, output all the contiguous substrings of length n
    in that string in the order that they appear.
    """
    if (length > len(series)) or (length <= 0):
        raise ValueError("invalid length")

    return [series[i: length+i] for i in range(0, len(series)) if (length + i) <= len(series)]