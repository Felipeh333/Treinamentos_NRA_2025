def palindromo(frase):
    frase = frase.replace(' ', '').lower()
    return frase == frase[::-1]

texto = input('Digite uma frase: ')
if palindromo(texto) ==  True:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')