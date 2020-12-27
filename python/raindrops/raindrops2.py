def convert(number):

    s = ""

    if (number % 3) == 0:
        s += "Pling"
    if (number % 5) == 0:
        s += "Plang"
    if (number % 7) == 0:
        s += "Plong"
    if s=="":
        s=str(number)

    return s

if __name__ == "__main__":
    print(convert(21))