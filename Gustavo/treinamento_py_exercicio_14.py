# Autoria:Gustavo Leal Malafaia
# Data:19/05/2025
# Objetivo do programa: Detectar se uma frase é um palíndromo

def checar_palindromo(frase):

    frase_minuscula = frase.lower()
    frase_sem_espacos = frase_minuscula.replace(' ', '')

    if frase_sem_espacos == frase_sem_espacos[::-1]:
        return True
    else:
        return False


frase_de_entrada = input('Entre com uma frase: ')

print(checar_palindromo(frase_de_entrada))
