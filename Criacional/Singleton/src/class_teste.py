class Conversa:

    def __init__(self, mensagem):
        self.mensagem = mensagem

    def falar(self):
        print(self.mensagem)

    def nova_mensagem(self, nova_mensagem):
        self.mensagem = nova_mensagem