def is_armstrong_number(number):
    """
    An Armstrong number is a number that is the sum of its own digits each raised
    to the power of the number of digits.
    Example: (1) 9 = 9^1 = 9, (2) 10 != 1^2 + 0^2 = 1
    Function that determines whether a number is an Armstrong number.
    """
    str_number = str(number)
    power = len(str_number)
    check = sum([int(str_number[i]) ** power for i in range(len(str_number))])
    return (check == number)