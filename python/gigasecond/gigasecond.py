from datetime import timedelta

def add(moment):
    """
    Given a moment, determine the moment that would be after a gigasecound has passed.
    """
    return moment + timedelta(0, 10**9)