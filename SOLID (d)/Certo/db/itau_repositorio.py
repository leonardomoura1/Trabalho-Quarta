class ItauRepositorio:
    def depositar(self, dado) -> None:
        print("Depositando R$ {} na Conta do itau".format(dado))
    
    def transferir(self, dado) -> None:
        print("Transferencia de R$ {} do Itau para o Banco do Brasil".format(dado))
    
    def buscar_saldo_conta(self, dado) -> None:
        print("O Saldo da Conta do itau é R$ {}".format(dado))
    
    def buscar_saldo_cartão(self, dado) -> None:
        print("O Saldo do Cartão do itau é R$ {}".format(dado))
    