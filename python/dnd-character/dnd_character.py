from math import floor
from random import randint

class Character:
    """
    Scores of the abilities: 6 times (one for each ability): Rolling four 6-sided dice and record the sum 
        of the largest three dice
    Initial hitpoints: 10 + your character's constitution modifier
    Constitution modifier: (character's constitution - 10) * 0.5 and round down
    """
    def __init__(self):
        self.strength = sum(sorted([randint(1, 6) for _ in range(4)])[-3:])
        self.dexterity = sum(sorted([randint(1, 6) for _ in range(4)])[-3:])
        self.constitution = sum(sorted([randint(1, 6) for _ in range(4)])[-3:])
        self.intelligence = sum(sorted([randint(1, 6) for _ in range(4)])[-3:])
        self.wisdom = sum(sorted([randint(1, 6) for _ in range(4)])[-3:])
        self.charisma = sum(sorted([randint(1, 6) for _ in range(4)])[-3:])
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self, ability="strength"):
        return getattr(self, ability)

def modifier(number):
    return floor((number - 10) * 0.5)

