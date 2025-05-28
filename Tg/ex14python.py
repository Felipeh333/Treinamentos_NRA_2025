frase = input('Digite uma frase: ').strip().lower().replace(' ', '')

def palindromo(frase):
    if frase == frase[::-1]:
       print('Tem-se um palindromo')
    else:
        print('Não temos um palindromo')

palindromo(frase)
