from src import Aventureiro, Magia,UsoArco, LutaEspada, Curar, LutaMarchado, UsoBesta
import random

cavaleiro = Aventureiro(LutaEspada(random.randint(0 , 99)))
arqueiro = Aventureiro(UsoArco(random.randint(0 , 99)))
besteiro = Aventureiro(UsoBesta(random.randint(0 , 99)))
curandeiro = Aventureiro(Curar(random.randint(0 , 99)))
mago = Aventureiro(Magia(random.randint(0 , 99)))
cavaleiroMarchado = Aventureiro(LutaMarchado(random.randint(0 , 99)))

print("\nVez do Cavaleiro1:")
cavaleiro.attributos()
cavaleiro.acao()

input("\nPressione qualquer tecla para continuar...")

print("\nVez do Besteiro:")
besteiro.attributos()
besteiro.acao()

input("\nPressione qualquer tecla para continuar...")

print("\nVez do Mago:")
mago.attributos()
mago.acao()

input("\nPressione qualquer tecla para continuar...")

print("\nVez do Cavaleiro2:")
cavaleiroMarchado.attributos()
cavaleiroMarchado.acao()

input("\nPressione qualquer tecla para continuar...")

print("\nVez do Arqueiro:")
arqueiro.attributos()
arqueiro.acao()

input("\nPressione qualquer tecla para continuar...")

print("\nVez do Curandeiro:")
curandeiro.attributos()
curandeiro.acao()