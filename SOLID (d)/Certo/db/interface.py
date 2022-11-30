from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def depositar(self, dado) -> None:
        pass
    
    @abstractmethod
    def transferir(self, dado) -> None:
        pass
    
    @abstractmethod
    def buscar_saldo_conta(self, dado) -> None:
        pass
    
    @abstractmethod
    def buscar_saldo_cartão(self, dado) -> None:
       pass