nome = str(input('Digite o seu nome completo, separando com espaço: '))
print()
print(f'Nome: {nome.title()}')
print(f'O nome tem {len(nome.replace(' ',''))} letras.')
print(f'O primeiro nome tem {len(nome.split(' ', 1)[0])} letras')