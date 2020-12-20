# Game status categories


STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.unguessed_chars = set(self.word)


    def guess(self, char):
        # Check the status
        if self.status == STATUS_LOSE:
            raise ValueError('The game is over! Try again.')
        elif self.status == STATUS_WIN:
            raise ValueError('You won already! Go home.')

        if char in self.unguessed_chars: # right guess
            self.unguessed_chars.remove(char)
        else: # failure
            self.remaining_guesses -= 1
        self.get_status()


    def get_masked_word(self):
        return "".join(["_" if char in self.unguessed_chars else char for char in self.word])


    def get_status(self):
        if len(self.unguessed_chars) == 0:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        return self.status