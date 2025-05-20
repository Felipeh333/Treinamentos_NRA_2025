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

produto1 = Produto('Pão', 10)
produto2 = Produto('Leite', 15)

carrinho = CarrinhoDeCompras()
carrinho.inserir_produto(produto1)

carrinho.listar_produtos()
print('Valor total da compra:', carrinho.valor_compra())