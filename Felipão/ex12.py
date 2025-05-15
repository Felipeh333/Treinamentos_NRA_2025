nome = str(input('Qual seu nome? '))

length_inteiro = len(nome.replace(' ', ''))
length_primeiro = len(nome.split(' ')[0])

print(nome.upper())
print(nome.lower())
print(length_inteiro)
print(length_primeiro)