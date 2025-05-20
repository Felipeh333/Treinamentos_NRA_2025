class Caneta:
    def __init__(self, cor, marca):
        self.__cor = cor
        self.__marca = marca

    def escrever(self):
        print('Caneta {} está escrevendo na cor {}'.format(self.__marca, self.__cor))


class Escritor:
    def __init__(self, nome):
        self.__caneta = None
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def novo(self):
        print(f'{self.nome} está escrevendo novo livro')

    @property
    def caneta(self):
        return self.__caneta
    
    @caneta.setter
    def caneta(self, caneta):
        self.__caneta = caneta

caneta1 = Caneta('azul', 'bic')
escritor1 = Escritor('Felipe')

escritor1.caneta = caneta1
escritor1.caneta.escrever()
