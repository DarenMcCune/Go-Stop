import random

class Deck:
    def __init__(self):
        self.deck=list(range(48))
        random.shuffle(self.deck)