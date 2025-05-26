# Autoria:Gustavo Leal Malafaia
# Data:25/05/2025
# Objetivo do progama: Exemplificar herança entre classes

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


Pessoa1 = Pessoa('Gustavo', 20)

Aluno1 = Aluno('Juca', 19)

Cliente1 = Cliente('Joca', 18)

Aluno1.falar()

# Testes emm que os métodos de uma subclasse não são aplicáveis a outras subclasses e também não a superclasse
# Cliente1.estudar()
# Pessoa1.estudar()
# Pessoa1.comprar()
