def is_valid(isbn):
    """Check if the provided string is a valid ISBN-10"""

    isbn = isbn.replace("-", "")
    if (
        (not isbn) 
        or (len(isbn) != 10) 
        or (not isbn[:-1].isdecimal())
    ):
        return False

    rng = reversed(range(2, 11))
    lin_comb = sum([int(l) * r for l, r in zip(isbn[:-1], rng)])

    if isbn[-1] == "X":
        lin_comb += 10
    elif isbn[-1].isdecimal():
        lin_comb += int(isbn[-1])
    else:
        return False

    return (lin_comb % 11 == 0)