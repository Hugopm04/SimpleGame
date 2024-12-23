from abc import ABC, abstractmethod
class Card(ABC):
    @staticmethod
    @abstractmethod
    def possible_values():
        pass

    @staticmethod
    @abstractmethod
    def possible_suits():
        pass


    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    @property
    def value(self):
        return(self.value)
    
    @property
    def suit(self):
        return(self.suit)
    
    @value.setter #No setter.
    def value(self, a): 
        pass

    @suit.setter #No setter.
    def suit(self, a):
        pass