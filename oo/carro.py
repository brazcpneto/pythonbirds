"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1. Motor
2. Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1. Atributo de dado velocidade
2. Método acelerar, que deverá incremetar a velocidade de uma unidade
3. Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

1. Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2. Método girar_a_direita
3. Método girar_a_esquerda

       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

class Motor:
    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade == 1:
            self.velocidade = 0
        else:
            self.velocidade -= 2

class Direcao:
    def __init__(self, valor = 'Norte'):
        self.valor = valor

    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'

    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Norte'