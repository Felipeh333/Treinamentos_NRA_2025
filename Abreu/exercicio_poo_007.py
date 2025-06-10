class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = __class__.__name__ # nome da classe
    
    def falar(self):
        print(f'{self.nome} está falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando...')

p1 = Pessoa('Dino', 17)
p1.falar()

a1 = Aluno('Pedro', 18)
a1.falar()
a1.estudar()

c1 = Cliente('Victor', 18)
c1.falar()
c1.comprar()
