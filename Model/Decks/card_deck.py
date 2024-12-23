from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from Model.Cards.card import Card
from random import shuffle as random_shuffle

card_t = TypeVar('card_t', bound=Card)

class CardDeck(ABC, Generic[card_t]): # Abstract
    def __init__(self, n_decks : int, card_type : card_t) -> None:
        self.deck = []
        self.n_decks = n_decks
        self.card_type = card_type

        self.fill_deck()

    def fill_deck(self) -> None:
        values = self.card_type.possible_values()
        suits = self.card_type.possible_suits()

        for i in range(self.n_decks):
            for value in values:
                for suit in suits:
                    self.deck.append(self.card_type(value, suit))
    
        self.shuffle()

    def shuffle(self) -> None:
        random_shuffle(self.deck)
    
    def draw_card(self) -> card_t:
        card = self.deck.pop()
        return(card)

    def empty(self) -> bool:
        if (len(self.deck) == 0):
            return(True)
        else:
            return(False)