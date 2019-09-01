import random


class Deck:
    NUMBER_MASK = 0b11
    MONTH_MASK = 0b111100
    DECEMBER = 0b111100

    BANNERS = (1, 5, 9, 13, 17, 21, 25, 33, 37, 47)
    HONG_DAN_BANNERS=(1,5,9)
    CHEONG_DAN_BANNERS=(21, 33, 37)
    CHO_DAN_BANNERS=(13, 17, 25)

    BRIGHTS = (0, 8, 28, 40, 44)
    ANIMALS = [4, 12, 16, 20, 24, 28, 32, 40]
    GODORI=(4, 12, 28)
    FLEX=32
    FISHERMAN=44
    DOUBLE_JUNK=[43, 47]


    def __init__(self):
        self.draw_pile = list(range(48))
        random.shuffle(self.draw_pile)

    @staticmethod
    def is_junk(card):
        if card & Deck.NUMBER_MASK > 1 and not Deck.is_december(card):
            return True

    @staticmethod
    def is_december(card):
        return card & Deck.MONTH_MASK == Deck.MONTH_MASK

    def switch_flex(self):
        pass

class Player:
    pass


class Engine:


    def __init__(self):
        pass

    def match_card(self, player, card_in_hand, card_on_table):
        pass

    def place_card(self, player, card):
        pass

    def go(self, player):
        pass

    def stop(self, player):
        pass

    def score(self):
        pass