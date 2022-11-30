from .interfaces import Ihabilidade

class LutaMarchado(Ihabilidade):
    def __init__(self, nivel):
        self.nivel = nivel
    
    def comportamento(self):
        print("Lutar com Marchado")
    
    def nivel_atributo(self):
        print('Nivel de uso Marchado: {}'.format(self.nivel))