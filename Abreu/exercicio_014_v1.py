#funções do código
def palindromo(frase):
    frase = (frase.lower()).replace(' ', '')
    tamanho_frase = len(frase)
    n = True

    for i in range(tamanho_frase):
        n = n and frase[i] == frase[tamanho_frase - 1]
        tamanho_frase -= 1

    return n 

# perguntar a frase e ajeitá-la para análise
frase = input("Digite uma frase: ")

analise = palindromo(frase)
if analise == True:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo')
