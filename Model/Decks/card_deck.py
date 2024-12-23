from abc import ABC, abstractmethod
from typing import TypeVar, Generic
import Cards.card as card

card_t = TypeVar('card_t', bound=card.Card)

class CardDeck(ABC, Generic[card_t]): #<<Abstract>>
    def __init__(self, n_decks : int, card_type : card_t):
        self.deck = []
        self.n_decks = n_decks
        self.card_type = card_t

    def fill_deck(self):
        values = self.card_type.possible_value()
        
