""" Yacht game """

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == 0:
        return 50 if len(set(dice)) == 1 else 0

    if category in range(1, 7):
        return category * dice.count(category)

    if category == 7: # Full House
        counts = {d: dice.count(d) for d in dice}
        if set([2, 3]).issubset(set(counts.values())):
            return sum(dice)
        return 0

    if category == 8: # Four of a kind
        if dice.count(sorted(dice)[1]) >= 4:
            return 4 * sorted(dice)[1]
        return 0

    if category == 9:  # Little straight
        return (sorted(dice) == [1, 2, 3, 4, 5]) * 30

    if category == 10:  # Big straight
        return (sorted(dice) == [2, 3, 4, 5, 6]) * 30

    if category == 11:
        return sum(dice)