#outro código, mas agora invertendo a função
#declarar funções
def palindromo(frase):
    frase = (frase.lower()).replace(' ', '')
    frase_invertida = ''
    tamanho = len(frase)
    
    for i in range(tamanho):
        frase_invertida += frase[tamanho - 1]
        tamanho -= 1
    
    if frase_invertida == frase:
        return 'A frase é um palíndromo!'
    else:
        return 'A frase não é um palíndromo!'

frase = input('Digite uma frase: ')

resultado = palindromo(frase)
print(resultado)
