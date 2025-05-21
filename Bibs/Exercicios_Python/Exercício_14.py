# Desenvolvido por Beatriz Matias
# Exercício 14

def palindromo(frase):
    frase_normal = frase.replace(" ", "").upper()
    if frase_normal == frase_normal[::-1]:  # lembrar texto[início:fim:passo] nesse caso coloco texto[fim:início:passo] porque o passo é negativo e inverte a string
        return True
    else:
        return False

texto = input("Digite uma frase: ")

if palindromo(texto):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")