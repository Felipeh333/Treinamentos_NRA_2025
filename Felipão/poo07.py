class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando')

pessoa1 = Pessoa('Felipe', 20)
aluno1 = Aluno('Jorge', 10)
cliente1 = Cliente('Homero', 25)

pessoa1.falar()

aluno1.falar()
aluno1.estudar()

cliente1.falar()
cliente1.comprar()