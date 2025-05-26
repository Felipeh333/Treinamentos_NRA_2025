# Autoria:Gustavo Leal Malafaia
# Data:25/05/2025
# Objetivo do progama:Exemplificar agregação de classes

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def valor_compra(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


C1 = CarrinhoDeCompras()

C2 = CarrinhoDeCompras()

P1 = Produto('Nescau', 10)

P2 = Produto('Leite', 5)

C2.inserir_produto(P1)
C2.inserir_produto(P2)

C1.listar_produtos()
C2.listar_produtos()
