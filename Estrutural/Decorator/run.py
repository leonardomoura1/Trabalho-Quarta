def decorator(funcao):
    def wrapper(*arg, **kwargs):
        print('aaaaaaAAAAAAAAAAAAAAaaaaaaaaa')
        funcao(*arg, **kwargs)  # Executa a função
    return wrapper

class minha_classe:
    @decorator
    def metodo(self):
        print('Estou na minha classe e ela e minha saia')


cl = minha_classe()
cl.metodo()