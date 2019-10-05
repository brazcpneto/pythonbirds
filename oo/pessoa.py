class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico(a, b):
        return a + b

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    pessoa = Homem('Anonimo')
    print(isinstance(pessoa,Pessoa))