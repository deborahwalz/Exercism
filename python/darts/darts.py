import math

def score(x, y):
    """
    Function that returns the earned points in a singlr toss of a Darts game.
    The outer circle has a radius of 10 units (this is equivalent to the total
    radius of the entire target).
    The middle circle has a radius of 5 units and the inner circle a radius of 1.
    The center point has the coordinates (0,0)
    """
    # Compute the distance
    distance = math.sqrt(x**2 + y**2)

    # Check the score
    if distance <= 1: # inner circle
        points = 10
    elif (distance > 1) and (distance <= 5): # middle circle
        points = 5
    elif (distance > 5) and (distance <= 10): # outer circle
        points = 1
    else:
        points = 0 # outside
    return points