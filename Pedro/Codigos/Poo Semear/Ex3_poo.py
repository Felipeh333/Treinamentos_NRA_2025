class BaseDeDados():
    def __init__(self):
        self.dados = {}

    def inserir_clientes(self,id,nome):
        self.dados.update({id:nome})
    
    def lista_clientes(self):
        for id,nome in self.dados.items():
            print(id,nome)

b1 = BaseDeDados()
b1.inserir_clientes(1,"Pedro")
b1.inserir_clientes(2,"Nanda")
b1.lista_clientes()

