class BaseDeDados:
    def __init__(self):
        self.__dados = {'clientes': {}}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]
    

db = BaseDeDados()
db.__dados = {'clientes': {1: 'Felipe'}} # Não funciona porque __dados foi encapsulada
db.inserir_clientes(1, 'Felipe') # Funciona por que acessa um método público, dentro da classe, que tem acesso a __dados
db.lista_clientes()