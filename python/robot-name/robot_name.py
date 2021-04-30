import string
import random

from datetime import datetime

class Robot:
    def __init__(self):
        self.create_name()

    def create_name(self):
        random.seed(datetime.now())
        letters = random.sample(string.ascii_uppercase, 2)
        digits = random.sample("0123456789", 3)
        self.name = "".join(letters +  digits)

    def reset(self):
        self.create_name()