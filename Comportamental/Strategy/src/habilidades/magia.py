from .interfaces import Ihabilidade

class Magia(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel
    
    def comportamento(self):
        print("Atacar com Magia")
    
    def nivel_atributo(self):
        print('Nivel da Magia: {}'.format(self.nivel))