# Autoria:Gustavo Leal Malafaia
# Data:25/05/2025
# Objetivo do progama:Exemplificar composição de classes

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}, {self.estado} FOI APAGADA')


cliente1 = Cliente('Gustavo', 20)

cliente1.insere_endereco('São Carlos', 'São Paulo')

cliente1.lista_enderecos()
