# Autoria:Gustavo Leal Malafaia
# Data:25/05/2025
# Objetivo do progama:Exemplificar associação de classes

class Caneta:

    def __init__(self, marca, cor):
        self.__marca = marca
        self.__cor = cor

    def escrevendo(self):
        print(f'Caneta {self.__marca} está escrevendo na cor {self.__cor}')


class Escritor:
    def __init__(self, nome, caneta):
        self.__nome = nome
        self.caneta = caneta

    @property
    def nome(self):
        return self.__nome

    def novo(self):
        print(f'{self.nome} está escrevendo novo livro')


c1 = Caneta('bic', 'azul')

Escritor1 = Escritor('Joãozinho', c1)

Escritor1.caneta.escrevendo()
