class BasedeDados:
    def __init__(self):
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados

    # metodo de instancia: inserir cliente
    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})

    # metodo de instancia: lista de clientes
    def lista_clientes(self):
        for (id, nome) in self.__dados['clientes'].items(): 
            print(id, nome)

    # metodo de instancia: apagar cliente
    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]

# codigo principal
base1 = BasedeDados()

base1.inserir_clientes(1, 'Pedro')
base1.inserir_clientes(2, 'Victor')
base1.inserir_clientes(3, 'Dino')
base1.inserir_clientes(4, 'Sud')
base1.inserir_clientes(5, 'Mochila')

base1.__dados = 'Um valor qualquer'
print(base1.__dados)

base1.lista_clientes()
print(base1._BasedeDados__dados)
print(base1.dados)
