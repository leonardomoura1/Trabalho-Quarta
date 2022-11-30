from abc import ABC, abstractmethod

class Animais(ABC):

    @abstractmethod
    def carnivoro(self):
        raise 'Should implement carnivoro method'

    @abstractmethod
    def herbivoro(self):
        raise 'Should implement herbirovo method'

    