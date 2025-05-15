class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*percentual / 100)

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @property
    def preco(self):
        return self._preco
    
    @nome.setter
    def nome(self, id):
        if id != id.upper():
            id = id.upper()
        self._nome = id

    @property
    def nome(self):
        return self._nome

