class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self,cidade,estado):
        self.enderecos.append(Endereco(cidade,estado))
    
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f"{self.nome} foi apagado")

class Endereco:
    def __init__(self,cidade,estado):

        self.cidade = cidade
        self.estado = estado

c1 = Cliente("Pedro", 19)
c1.inserir_endereco("SAJ","Bahia")
c1.inserir_endereco("Tokyo","Japão")
c1.inserir_endereco("São Carlos","São Paulo")

c1.lista_enderecos()

