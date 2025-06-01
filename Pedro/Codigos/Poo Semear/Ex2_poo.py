class Produto:

    def __init__(self,nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome.upper()
        
p1 = Produto("Pedro")
print(p1.nome)
