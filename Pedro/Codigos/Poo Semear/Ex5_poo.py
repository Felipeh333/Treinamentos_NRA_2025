class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self,produto):
        self.produtos.append(produto)

    def listar_podutos(self):
        for produto in self.produtos:
            print(produto.nome,produto.valor)

    def valor_compra(self):
        total = 0
        for produto in self.produtos:
            total = total + produto.valor
    
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

p1 = Produto("maça", 12)
p2 = Produto("banana", 15)
p3 = Produto("pera", 8)
p4 = Produto("lasanha", 25)

c1 = CarrinhoDeCompras()

c1.inserir_produtos(p1)
c1.inserir_produtos(p2)
c1.inserir_produtos(p3)
c1.inserir_produtos(p4)

c1.listar_podutos()
