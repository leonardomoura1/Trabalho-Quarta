class BBRepositorio:
    def depositar(self, dado) -> None:
        print("Depositando R$ {} na Conta do Banco do Brasil".format(dado))
    
    def transferir(self, dado) -> None:
        print("Transferencia de R$ {} do Banco do Brasil para o Itau".format(dado))
    
    def buscar_saldo_conta(self, dado) -> None:
        print("O Saldo da Contado Banco do Brasil é R$ {}".format(dado))
    
    def buscar_saldo_cartão(self, dado) -> None:
        print("O Saldo do Cartãodo Banco do Brasil é R$ {}".format(dado))
    