from typing import Type
from db.itau_repositorio import ItauRepositorio
import random

class Usuario:
    def __init__(self, repositorio: Type[ItauRepositorio]):
        self.repositorio = repositorio

    def depositar(self, dado: any) -> None:
        self.repositorio.depositar(dado)

    def transferir(self, dado: any) -> None:
        self.repositorio.transferir(dado)

    def buscar_saldo_conta(self, dado: any) -> None:
        return self.repositorio.buscar_saldo_conta(dado)

    def buscar_saldo_cartão(self, dado: any) -> None:
        self.repositorio.buscar_saldo_cartão(dado)


usuario = Usuario(ItauRepositorio())
print("*-*")
usuario.buscar_saldo_conta(round(random.uniform(0.0 , 999.9), 2))
print("*-*")
usuario.buscar_saldo_cartão(round(random.uniform(0.0 , 999.9),2))
print("*-*")
usuario.depositar(100)
print("*-*")
usuario.transferir(100)
print("---------------------------------")