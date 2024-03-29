import random


class Deck:
    NUMBER_MASK = 0b11
    MONTH_MASK = 0b111100
    DECEMBER = 0b111100

    BANNERS = set([1, 5, 9, 13, 17, 21, 25, 33, 37, 47])
    HONG_DAN_BANNERS=set([1,5,9])
    CHEONG_DAN_BANNERS=set([21, 33, 37])
    CHO_DAN_BANNERS=set([13, 17, 25])

    BRIGHTS = set([0, 8, 28, 40, 44])
    ANIMALS = set([4, 12, 16, 20, 24, 28, 32, 40])
    GODORI=set([4, 12, 28])
    FLEX=32
    FISHERMAN=44
    DOUBLE_JUNK=set([43, 47])


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

    @staticmethod
    def is_banner(card):
        return card in Deck.BANNERS

    @staticmethod
    def is_bright(card):
        return card in Deck.BRIGHTS

    @staticmethod
    def is_flex(card):
        return card==Deck.FLEX

    @staticmethod
    def cards_contain_godori(cards):
        return Deck.GODORI.issubset(cards)


class Player:
    def __init__(self, minimum_points=3):
        self.hand=[]
        self.captured_cards={'junk':set(), 'brights':set(), 'animals':set(), 'banners':set()}
        self.next_stop_chance=minimum_points

    def take_turn(self, cards_on_table):
        pass


class Engine:


    def __init__(self, num_players):
        self.draw_pile = Deck()
        self.players=[Player for i in range(num_players)]

        pass

    def match_card(self, player, card_in_hand, card_on_table):
        pass

    def place_card(self, player, card):
        pass

    def go(self, player):
        pass

    def flip_card(self):
        pass

    def stop(self, player):
        pass

    def score(self):
        pass