from Model.Cards.spanish_card import SpanishCard
from Model.Decks.card_deck import CardDeck

class SpanishDeck(CardDeck):
    def __init__(self, n_decks : int):
        super().__init__(n_decks, SpanishCard)