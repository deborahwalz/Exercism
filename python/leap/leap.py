def leap_year(year):
    """
    Check if the given year is a leap year.
    Leap year: every year that is evenly divisible by 4,
        except every year that is evenly divisible by 100,
            unless the year is also evenly divisible by 400.
    """
    # Conditions
    is_div_4 = not (year % 4)
    is_div_100 = not (year % 100)
    is_div_400 = not (year % 400)
    
    # non_leap years:
    non_leap = is_div_100 and (not is_div_400)

    return is_div_4 and ((not is_div_100) or is_div_400)