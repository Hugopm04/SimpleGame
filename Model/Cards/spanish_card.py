from card import Card
from random import randint
from spanish_suits import SpanishSuit

class SpanishCard(Card):
    #Override
    @staticmethod
    def possible_values():
        values = []
        for i in range(1, 11, 1):
            if i < 8:
                values.append(i)
            else:
                values.append(i+2)
        return(values)

    #Override
    @staticmethod
    def possible_suits():
        suits = []
        suits.append(SpanishSuit.CLUBS)
        suits.append(SpanishSuit.CUPS)
        suits.append(SpanishSuit.GOLDS)
        suits.append(SpanishSuit.SWORDS)
        return(suits)

    def __init__(self, value, suit):
        super.__init__(value, suit)