def convert(number):

    is_3 = (number % 3) == 0
    is_5 = (number % 5) == 0
    is_7 = (number % 7) == 0

    s = ""

    if is_3:
        s += "Pling"
    if is_5:
        s += "Plang"
    if is_7:
        s += "Plong"
    if not (is_3 or is_5 or is_7):
        s=str(number)

    return s