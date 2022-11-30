from interface import Animais

class Leao(Animais):
    def carnivoro(self):
        print('Leão é carnívoro')
    def herbivoro(self):
        None

class Veado(Animais):
    def herbivoro(self):
        print('Veado é herbívoro')
    def carnivoro(self):
        None

