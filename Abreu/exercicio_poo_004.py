class Caneta:
    def __init__(self, marca, cor):
        self.__marca = marca
        self.__cor = cor
    
    @property
    def cor(self):
        return self.__cor
    
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print(f'Caneta {self.__marca} está escrevendo na cor {self.__cor}')

class Escritor:
    def __init__(self, nome, ferramenta):
        self.__nome = nome
        self.__ferramenta = ferramenta

    @property
    def nome(self):
        return self.__nome
    
    @property
    def caneta(self):
        return self.__ferramenta


caneta1 = Caneta('Bic', 'Preta')
caneta1.escrever()

escritor1 = Escritor('Machado', caneta1)
escritor1.caneta.escrever()
