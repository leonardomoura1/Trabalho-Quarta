from abc import ABC, abstractmethod

class Animais_carnivoros(ABC):

    @abstractmethod
    def carnivoro(self):
        raise 'Should implement carnivoro method'

class Animais_herbivoros(ABC):
    @abstractmethod
    def herbivoro(self):
        raise 'Should implement herbirovo method'

    