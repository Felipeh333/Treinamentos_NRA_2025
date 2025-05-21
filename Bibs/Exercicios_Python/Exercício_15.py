# Desenvolvido por Beatriz Matias
# Exercício 15

def maior(valores):
    if len(valores) == 0:
        print("Nenhum valor informado.")
        return

    maior_valor = valores[0]
    for numero in valores:
        if numero > maior_valor:
            maior_valor = numero

    print("Os valores informados foram:", valores)
    print("O maior valor é:", maior_valor)

valores = input("Digite números separados por espaço: ")
maior(valores)

# esse aqui não deu muito certo, voltar para consertar