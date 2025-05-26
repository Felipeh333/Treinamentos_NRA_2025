# Autoria:Gustavo Leal Malafaia
# Data:25/05/2025
# Objetivo do progama:Exemplificar encapsulamento

class BaseDeDados:

    def __init__(self):
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

    @property  # Método getter para ver os dados da variável encapsulada
    def dados(self):
        return self.__dados.copy()


b1 = BaseDeDados()

b1.inserir_clientes(23, 'joca')

b1.lista_clientes()

print(b1.dados)  # Acesso dos dados encapsulados
