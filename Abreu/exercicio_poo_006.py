class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def inserir_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado)) # cria um objeto, mas sem identificador associado

    def lista_enderecos(self):
        print(f'\n{self.nome}:')
        for endereco in self.endereco:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} foi apagado!')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    def __del__(self):
        print(f'{self.cidade} / {self.estado} foi apagado!')

cliente1 = Cliente('Pedro', 18)
cliente1.inserir_endereco('Brasília', 'DF')
cliente1.inserir_endereco('São Carlos', 'SP')
cliente1.lista_enderecos()
