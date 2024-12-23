from abc import ABC, abstractmethod
from enum import Enum

class Card(ABC):
    @staticmethod
    @abstractmethod
    def possible_values() -> list[int]:
        pass

    @staticmethod
    @abstractmethod
    def possible_suits() -> list[Enum]:
        pass


    def __init__(self, value :int, suit :Enum):
        self._value = value
        self._suit = suit
    
    @property
    def value(self):
        return(self._value)
    
    @property
    def suit(self):
        return(self._suit)
    
    @value.setter #No setter.
    def value(self, a:int): 
        pass

    @suit.setter #No setter.
    def suit(self, a:Enum):
        pass
    
    def __str__(self):
        s = str(self._value) + " de " + str(self._suit.name)
        return(s)