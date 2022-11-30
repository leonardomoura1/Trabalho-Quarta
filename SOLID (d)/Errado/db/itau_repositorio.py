class ItauRepositorio:
    def depositar(self, dado) -> None:
        print("Depositando {} na Conta".format(dado))
    
    def transferir(self, dado) -> None:
        print("Transferencia de {} para outra conta".format(dado))
    
    def buscar_saldo_conta(self, dado) -> None:
        print("O Saldo da Conta é R$ {}".format(dado))
    
    def buscar_saldo_cartão(self, dado) -> None:
        print("O Saldo do Cartão é R$ {}".format(dado))
    