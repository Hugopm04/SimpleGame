from Model.Cards.spanish_card import SpanishCard
from Model.Decks.card_deck import CardDeck

class Test():
    @staticmethod
    def main():
        Test.test_cards()
        Test.test_decks()

    @staticmethod
    def test_cards():
        print("Posibles valores de la baraja española: ")
        print(SpanishCard.possible_values())
        print("Posibles palos: ")
        print(SpanishCard.possible_suits())

    @staticmethod
    def test_decks():
        deck = CardDeck(1, SpanishCard)
        card = deck.draw_card()
        counter = 1
        print("Cogiendo una carta de la baraja, ha salido: " + str(card))
        while (not deck.empty()):
            card = deck.draw_card()
            print("Cogiendo una carta de la baraja, ha salido: " + str(card))
            counter += 1
        print("Baraja vacía, han salido " + str(counter) + " cartas.")

if __name__ == '__main__':
    Test.main()
