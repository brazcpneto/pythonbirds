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

if __name__ == '__main__':
    renzo = Pessoa(nome = 'Renzo', idade = 30)
    luciano = Pessoa(renzo, nome = 'Luciano', idade = 40)
    luciano.sobrenome = 'Ramalho'
    print(Pessoa.nome_e_atributos_de_classe())