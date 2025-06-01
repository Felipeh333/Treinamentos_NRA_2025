class Caneta:
    def __init__(self,cor,marca):
        self.cor = cor
        self.marca = marca

    def escrever(self):
        print(f"Caneta de marca {self.marca} está escrevendo na cor {self.cor}")

class Escritor:
    def __init__(self,nome):
        self.nome = nome
        self._caneta = None

    @property
    def caneta(self):
        return self._caneta

    @caneta.setter
    def caneta(self,caneta):
        self._caneta = caneta


caneta1 = Caneta("Preta", "Bic")
escritor1 = Escritor("Pedro")
escritor1.caneta = caneta1
escritor1.caneta.escrever()