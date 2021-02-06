def factors(value):
    if value == 1:
        return []
    elif value < 1:
        raise ValueError("Invalid value!")
    else:
        factors = []
        candidates = range(2, value+1)
        for candidate in candidates:
            while value % candidate == 0:
                value = value / candidate
                factors.append(candidate)
        return factors