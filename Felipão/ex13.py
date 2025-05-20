frase = str(input('Digite uma frase: ')).lower()

print('A letra "a" aparece {} vezes na frase.'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(frase.find('a')))
print('A letra "a" aparece pela última vez na posição {}.'.format(frase.rfind('a')))