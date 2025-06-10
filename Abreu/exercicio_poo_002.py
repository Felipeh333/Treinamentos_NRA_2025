class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    # metodo de instancia: desconto ao preco
    def desconto(self, percentual):
        self.preco = self.preco - self.preco*(percentual / 100)
        return self.preco
    
    # define-se o getter (atributo: nome)
    @property
    def nome(self):
        return self._nome

    # define-se o setter (atributo: nome)
    @nome.setter
    def nome(self, valor):
        if valor != valor.upper():
            valor = valor.upper()
        self._nome = valor

    # define-se o getter (atributo: preco)
    @property
    def preco(self):
        return self._preco

    # define-se o setter (atributo: preco)
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor
    

prod1 = Produto('Arroz', 'R$45.67') # exemplo ilustrativo
print(prod1.nome)
print(prod1.desconto(38)) # exemplo ilustrativo

