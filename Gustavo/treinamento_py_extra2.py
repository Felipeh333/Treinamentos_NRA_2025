# Autoria:Gustavo Leal Malafaia
# Data:25/05/2025
# Objetivo do progama:Exemplo de implementação dos métodos getter e setter de nome

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco -= (self.preco*percentual/100)

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.upper()


prod1 = Produto('Arroz', 'R$7')

print(prod1.nome)
