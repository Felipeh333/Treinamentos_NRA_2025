# Desenvolvido por Beatriz Matias
# Exercício 16

def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
            return n
        except:
            print("ERRADO! Digite um número inteiro válido!")

numero = leiaInt("Digite um número inteiro: ")
print("Você digitou o número:", numero)




