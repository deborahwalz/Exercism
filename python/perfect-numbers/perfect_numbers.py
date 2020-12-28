def classify(number):
    """
    Determine if a number is perfect, abundant or deficient.
    """
    if number <= 0:
        raise ValueError("Number is not a positive integer!")

    aliquot_sum = sum([i for i in range(1, number) if (number % i == 0)])
    
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    elif aliquot_sum < number:
       return "deficient"