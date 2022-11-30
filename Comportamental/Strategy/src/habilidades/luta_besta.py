from .interfaces import Ihabilidade

class UsoBesta(Ihabilidade):
    def __init__(self, nivel):
        self.nivel = nivel
    
    def comportamento(self):
        print("Atirar virotes")
    
    def nivel_atributo(self):
        print('Nivel de uso Arco: {}'.format(self.nivel))